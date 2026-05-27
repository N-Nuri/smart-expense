from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models

# Tạo bảng tự động
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Expense API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Smart Expense API is running!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}