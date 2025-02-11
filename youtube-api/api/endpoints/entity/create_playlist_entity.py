from pydantic import BaseModel


class item(BaseModel):
    playlist_name: str

class PlaylistItem(BaseModel):
    playlist_name: str
    playlist_musics : list