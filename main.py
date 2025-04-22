from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/videos")
def get_videos():
    return [
        {"id": 1, "title": "FastAPI Intro", "url": "https://www.w3schools.com/html/mov_bbb.mp4"},
        {"id": 2, "title": "React Basics", "url": "https://www.w3schools.com/html/movie.mp4"},
    ]

@app.post("/auth/login")
def login(username: str, password: str):
    if username == "admin" and password == "1234":
        return {"success": True}
    return {"success": False}
