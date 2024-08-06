from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def index():
    return 'Welcome to house data india.'


if __name__ == '__main__':
    uvicorn.run(app="app:app",reload=True)