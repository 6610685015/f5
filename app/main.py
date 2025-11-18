import models
import name
from database import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

HOST = "localhost"
PORT = "7000"

app = FastAPI()

origins = [
    f"http://{HOST}:{PORT}",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(name.router)


@app.get("/check")
def root():
    return {"message": "Health check"}
