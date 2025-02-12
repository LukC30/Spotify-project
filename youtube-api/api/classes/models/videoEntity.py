class VideoEntity():

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
    
    def get_entity(self, video_id : str):
        return {
                "snippet": {
                    "playlistId": self.__playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
    
        