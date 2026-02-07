from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/robots.txt")
async def robots():
    return FileResponse("static/robots.txt")


@app.get("/sitemap.xml")
async def sitemap():
    return FileResponse("static/sitemap.xml")


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse("/")
