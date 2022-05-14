from fastapi import FastAPI

app = FastAPI()


@app.get("/ping/")
def view():
    return {"message": "pong"}
