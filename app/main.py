from fastapi import FastAPI

APP_VERSION = "1.0.0"

app = FastAPI()

@app.get("/")
def read_root():
  return {
    "message": "Hello DevOps",
    "version": APP_VERSION
  }
