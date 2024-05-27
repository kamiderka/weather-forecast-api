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
        raise HTTPException(status_code=400, detail=err)
    
    forecast_df = await openMeteoClient.getForecast(latitude, longitude)
    forecast_df['energy'] = forecast_df['sunshineDuration'].apply(getEnergyFromSunlightDuration).round(2)
    forecast_df.drop("sunshineDuration", axis=1, inplace=True) 

    return forecast_df.to_dict(orient='records')
