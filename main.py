import uvicorn

from fastapi import FastAPI

app = FastAPI(
    title="SpotifyApi",
    description="Api para conversão de playlists",
    version="1.0.0"
)

@app.get("/", status_code=200)
def uauuu():
    return {"Message" : "Seja bem vindo!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)