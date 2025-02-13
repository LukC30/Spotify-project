from api.classes.service.playlistService import PlaylistService
from api.classes.models.playlistEntity import PlaylistEntity
from api.classes.models.videoEntity import VideoEntity


class PlaylistController:
    
    def __init__(self):
        self.playlist_service = PlaylistService()

    def create_playlist_and_insert_music(self, playlist_name, playlist):
        playlist_entity = PlaylistEntity(title=playlist_name, description="teste", videos=playlist)
        video_ids = self.playlist_service.search_musics(playlist_entity.get_videos())
        print(f"IDs da playlist: {video_ids}")

        playlist_id = self.playlist_service.create_playlist(playlist_entity)
        print(f"Playlist criada: {playlist_id}")
        video_entity = VideoEntity(playlist_id)
        self.playlist_service.add_musics_in_playlist(video_ids, video_entity)

        return {"Message" : "Talvez tenha dado certo"}
    
    def create_playlist(self, playlist_name):
        try:    
            playlist_entity = PlaylistEntity(title=playlist_name, description="teste", videos=[])
            print(playlist_entity)
            playlist_id = self.playlist_service.create_playlist(playlist_entity)
            print(playlist_id)
            return playlist_id
        except Exception as e:
            return(f"erro: {e}")
        
    def add_musics(self, playlist_id: str, playlist_musics: list[str]):
        try:
            xisde = VideoEntity(playlist_id)
            musics_ids = self.playlist_service.search_musics(playlist_musics)
            print(musics_ids)
            request = self.playlist_service.add_musics_in_playlist(musics_ids, xisde)
            return print(f"Achoquefoi: {request}")
        except Exception as e:
            return print(f"pelo visto nao edeu fudeu: {e}")