from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Issue 29 resolved"}
