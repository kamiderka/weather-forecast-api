from fastapi import APIRouter, HTTPException
from .client import OpenMeteoClient
from .utils import validateCoordinates, getEnergyFromSunlightDuration

forecast_router = APIRouter()

openMeteoClient = OpenMeteoClient()

# Type assertion of input from the client is performed by FastAPI 
@forecast_router.get("/forecast")
async def getForecastWithEnergy(latitude :float, longitude:float):
    ok, err = validateCoordinates(latitude, longitude)
    if not ok:
        raise HTTPException(status_code=422, detail=err)
    
    forecast = await openMeteoClient.getForecast(latitude, longitude)
    forecast['energy'] = [ getEnergyFromSunlightDuration(duration) for duration in forecast['sunshine_duration']]

    return forecast