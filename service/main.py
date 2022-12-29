from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Test World from sand1k!!!"}
