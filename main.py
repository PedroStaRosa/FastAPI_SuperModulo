from routes import called
from fastapi import FastAPI, Request
from database import create_tables
import time
from middleware import create_token,auth_middleware

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()

app.include_router(called.router)

@app.middleware("http")
async def log(request: Request, call_next):  # Transforme o middleware em uma função assíncrona
    start_time = time.time()
    print(f"Recebendo requisição: {request.method} {request.url}")

    response = await call_next(request)  # Aguarde a execução de call_next com await

    process_time = time.time() - start_time
    print(f"Finalizada em {process_time:.2f} segundos")

    return response

@app.middleware("http")
def  authenticate_request(request: Request, call_next):
    return auth_middleware(request,call_next)

@app.get("/")
def read_root():
    return {"message" : "api runningggg"}