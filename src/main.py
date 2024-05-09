from fastapi import FastAPI
from forecast.router import forecast_router

app = FastAPI()

app.include_router(forecast_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}