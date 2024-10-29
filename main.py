from routes import called
from fastapi import FastAPI
from database import create_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()


app.include_router(called.router)


@app.get("/")
def read_root():
    return {"message" : "api running"}