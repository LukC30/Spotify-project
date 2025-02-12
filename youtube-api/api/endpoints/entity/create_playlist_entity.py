from pydantic import BaseModel


class item(BaseModel):
    playlist_name: str

class PlaylistItem(BaseModel):
    playlist_name: str
    playlist_musics : list

class PlaylistMusics(BaseModel):
    playlist_id: str
    playlist_musics: list