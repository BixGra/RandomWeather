from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from src.tools import weather

app = FastAPI()
app.mount("/src", StaticFiles(directory="src"))


@app.get("/")
def get_method():
    return HTMLResponse(content=weather.weather(), status_code=200)
