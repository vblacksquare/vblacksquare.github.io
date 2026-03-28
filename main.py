
import fastapi
from fastapi.templating import Jinja2Templates


app = fastapi.FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: fastapi.Request):
    people = [
        {
            "first_name": "Denis",
            "last_name": "Minka",
        },
        {
            "first_name": "Matviy",
            "last_name": "Shevchenko",
        }
    ] * 1000

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "el_primo": people
        }
    )
