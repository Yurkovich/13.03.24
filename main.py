from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/submit_form")
def submit_form(title: str = Form(...), description: str = Form(...)):
    print(f"Title: {title}")
    print(f"Description: {description}")
    return {"message": "Форма удачно отправлена!"}
