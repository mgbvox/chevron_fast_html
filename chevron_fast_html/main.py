import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import numpy as np

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "demo": "hello world"}
    )


@app.get("/get-html", response_class=PlainTextResponse)
async def get_html():
    df = pd.DataFrame.from_records(np.random.random((5,5)))
    # This is where you define your HTML string that will be sent
    return f"<div>{df.to_html()}</div>"

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8123)
