from fastapi import APIRouter
from .openmeteoclient import OpenMeteoClient

forecast_router = APIRouter()

openMeteoClient = OpenMeteoClient()

@forecast_router.get("/forecast")
def getForecast(latitude :float, longitude:float):
    result = openMeteoClient.getForecast(latitude, longitude)
    return result



