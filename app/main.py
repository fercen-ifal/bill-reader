from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware

from routers import reader
from helpers.config import CONFIG

app = FastAPI(title=CONFIG["app_name"], description=CONFIG["app_desc"], version=CONFIG["app_version"],
              contact={"name": "João Pedro", "email": "jpnm1@aluno.ifal.edu.br"}, responses={404: {"message": "Rota não encontrada."}})
app.include_router(reader.router)


if CONFIG["is_prod"]:
    app.add_middleware(HTTPSRedirectMiddleware)

app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=CONFIG["allowed_origins"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RootResponse(BaseModel):
    app_name: str
    app_version: str
    environment: str


@app.get("/", description="Retorna informações úteis sobre o app.", response_model=RootResponse)
def root():
    return {"app_name": CONFIG["app_name"], "app_version": CONFIG["app_version"], "environment": CONFIG["env"]}


if __name__ == "__main__":
    uvicorn.run("main:app", host=CONFIG["host"], port=int(CONFIG["port"]),
                reload=CONFIG["is_dev"], server_header=False)
