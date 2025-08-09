from fastapi import FastAPI
from app.routers.generation import router as generation_router

app = FastAPI(title="Writing Assistant API")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

app.include_router(generation_router)
