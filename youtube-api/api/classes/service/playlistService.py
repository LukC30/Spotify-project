import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from api.classes.models.videoEntity import VideoEntity
from api.classes.models.playlistEntity import PlaylistEntity
import json

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

class PlaylistService:

    def __init__(self, credentials_file="credentials.json"):
        self.__credentials = self.__authenticate(credentials_file)
        self.youtube = googleapiclient.discovery.build("youtube", 'v3', credentials=self.__credentials)

    def __authenticate(self, credentials_file):
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
        flow.redirect_uri = "http://localhost:8080/oauth2callback"
        
        credentials = flow.run_local_server(port=8080)
        return credentials

    def search_music(self, music_name: str):
        request = self.youtube.search().list(q=music_name, part="snippet", type="video", maxResults=1)
        response = request.execute()
        return response["items"][0]["id"]["videoId"] if response["items"] else None

    def search_musics(self, music_list: list[str]) -> list:
        name_musics: list = []
        for music_id in music_list:
            name_musics.append(self.search_music(music_id))
        return name_musics

    def create_playlist(self, playlistEntity: PlaylistEntity):
        try:
            request = self.youtube.playlists().insert(part="snippet,status", body=playlistEntity.object_entity())
            response = request.execute()
            playlist_id = response.get("id")
            print(f"Playlist criada: {playlist_id}")
            return playlist_id
            # raise Exception("Playlist ID não encontrado.")
        except googleapiclient.errors.Error as e:
            return {"Error": f"Erro na criação da playlist: {e}"}

    def add_music_in_playlist(self, youtube_video_id: str, video_entity: VideoEntity):
        print(video_entity.get_entity(youtube_video_id))
        try:
            request = self.youtube.playlistItems().insert(part="snippet", body=video_entity.get_entity(youtube_video_id))
            print(video_entity.get_entity(youtube_video_id))
            request.execute()
            return request
        except googleapiclient.errors.Error as e:
            return {"message_error": f"Erro na inserção da playlist: {e}"}

    def add_musics_in_playlist(self, list_youtube_videos_id: list[str], video_entity: VideoEntity):
        for video_id in list_youtube_videos_id:
            self.add_music_in_playlist(video_id, video_entity)
        return {"Message":"Deu tudo certo parabens"}
