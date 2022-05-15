from fastapi import FastAPI

from random_quote.quote_router import router as random_quote_router

app = FastAPI()
app.include_router(random_quote_router)


@app.get("/ping/")
def view():
    """
    "GET /ping/"
    """
    return {"message": "pong"}
