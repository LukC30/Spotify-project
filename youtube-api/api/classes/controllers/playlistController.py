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
        print("Playlist criada")
        video_entity = VideoEntity(playlist_id)
        self.playlist_service.add_musics_in_playlist(video_ids, video_entity)

        return
    
    def create_playlist(self, playlist_name):
        try:    
            playlist_entity = PlaylistEntity(title=playlist_name, description="teste", videos=[])
            print(playlist_entity)
            playlist_id = self.playlist_service.create_playlist(playlist_entity)
            print(playlist_id)
            return playlist_id
        except Exception as e:
            return(f"erro: {e}")