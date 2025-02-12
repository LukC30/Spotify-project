from fastapi import APIRouter, Request
from api.endpoints.config.config_yt import url
from api.classes.controllers.playlistController import PlaylistController
from pydantic import BaseModel
from api.endpoints.entity.create_playlist_entity import item, PlaylistItem, PlaylistMusics


app = APIRouter()
playlist_controller = PlaylistController()


@app.get("/")
async def test():
    return {"Message" : "Hi bro"}

@app.post("/create")
def teste_criação_playlist(request: item):
    body = request
    print(body, body.playlist_name)
    try:
        id = playlist_controller.create_playlist(str(body.playlist_name))
        return print(f"VAMOOOOOOOOOOOOOOOOOOO toma ai o id: {id}")
    except Exception as e:
        return print(f"Deu erro, veja ai: {e}")

@app.post("/create_playlist")
def create_playlist_with_musics(request: PlaylistItem):
    body = request
    print(body, body.playlist_musics)
    try:
        id = playlist_controller.create_playlist_and_insert_music(str(body.playlist_name), body.playlist_musics)
        return print(f"VAMOOOOOOOOOOO: f{id}")
    except Exception as e:
        return print(f"erro: {e}")
    
@app.put("/insert_musics_in_playlist")
def insert_musics_in_playlist(request: PlaylistMusics):
    body = request
    
    musics = playlist_controller.add_musics(body.playlist_id, body.playlist_musics)
    print(f"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA: {musics}")
    


    
    