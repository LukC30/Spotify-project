from api.endpoints import playlist
from fastapi import APIRouter

routes = APIRouter()

routes.include_router(playlist.app, prefix="/playlist", tags="Playlist")