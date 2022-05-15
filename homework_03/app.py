from fastapi import FastAPI

from container.container_router import router as container_router
from random_quote.quote_router import router as random_quote_router

app = FastAPI()
app.include_router(container_router)
app.include_router(random_quote_router)


@app.get("/ping/")
def view():
    """
    "GET /ping/"
    """
    return {"message": "pong"}


@app.get("/")
def root():
    return {"message": "this is a root"}

