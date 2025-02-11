from enum import Enum
import json

class PrivacyStatus(Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    UNLISTED = "unlisted"


class PlaylistEntity():

    def __init__(self, title: str, description : str, privacy_status : PrivacyStatus = PrivacyStatus.PUBLIC, videos: list = []):
        self.__title = title
        self.__description = description
        self.__privacy_status = privacy_status.value
        self.__videos = videos
    
    def object_entity(self):
        return {
            "snippet": {
                "title": self.__title,
                "description": self.__description
            },
            "status": {
                "privacyStatus": self.__privacy_status
            }
        }

    
    def add_videos(self, videos: list):
        for video_name in videos:
            if video_name not in self.__videos:
                self.__videos.append(video_name)
                return f"Video adicionado"

    def remove_videos(self, videos: list):
        for video in videos:
            if video in videos:
                self.__videos.remove(video)
    
                return f"Video removido"
            
    def get_videos(self):
        return self.__videos
            
    def set_name(self, name: str):
        self.__title = name

    def get_name(self):
        return self.__title
    
    def set_description(self, description: str):
        self.__description = description
    
    def get_description(self):
        return self.__description
    