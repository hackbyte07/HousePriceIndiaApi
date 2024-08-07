from fastapi import FastAPI
import uvicorn
from routes import HousePriceRoute


app = FastAPI()


@app.get("/")
def index():
    return 'Welcome to house data india.'


app.include_router(HousePriceRoute.router)



if __name__ == '__main__':
    uvicorn.run(app="app:app",reload=True)