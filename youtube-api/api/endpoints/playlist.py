from fastapi import APIRouter, Request
from api.endpoints.config.config_yt import url
from api.classes.controllers.playlistController import PlaylistController
from pydantic import BaseModel

import requests

app = APIRouter()
playlist_controller = PlaylistController()

@app.get("/")
async def test():
    return {"Message" : "Hi bro"}

class item(BaseModel):
    playlist_name: str

@app.post("/create")
def teste_criação_playlist(request: item):
    body = request
    print(body, body.playlist_name)
    try:
        id = playlist_controller.create_playlist(str(body.playlist_name))
        return print(f"VAMOOOOOOOOOOOOOOOOOOO toma ai o id: {id}")
    except Exception as e:
        return print(f"Deu erro, veja ai: {e}")