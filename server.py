from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request


templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/")
def display(request : Request):
    return templates.TemplateResponse("index.html", {"request": request})
