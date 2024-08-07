from fastapi import FastAPI
import uvicorn
from routes import HousePriceRoute
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
        "http://localhost:8000",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


@app.get("/")
def index():
    return {'message':'Welcome to house data india.'}


app.include_router(HousePriceRoute.router)



if __name__ == '__main__':
    uvicorn.run(app="app:app",reload=True)