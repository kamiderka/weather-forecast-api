import openmeteo_requests
from fastapi import HTTPException
from typing import Tuple

from openmeteo_sdk import WeatherApiResponse

import requests_cache
from retry_requests import retry
import pandas as pd
from .utils import buildForecastQueryParams


class OpenMeteoClient:
    _url = "https://api.open-meteo.com/v1/forecast"

    def __init__(self) -> None:
        _cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        _retry_session = retry(_cache_session, retries = 5, backoff_factor = 0.2)
        self.client = openmeteo_requests.Client(session = _retry_session)


    async def getResponsesFromClient(self, url : str, params:str) -> WeatherApiResponse:
        try:
            responses = self.client.weather_api(self._url, params=params)
        except Exception as e:
            err_message = eval(str(e))['reason']
            raise HTTPException(status_code=400, detail=err_message)
        
        return responses
    
    async def parseResponseToDailyDict(self, response:WeatherApiResponse) -> pd.DataFrame:
        daily = response.Daily()

        daily_weather_code = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
        daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()
        daily_sunshine_duration = daily.Variables(3).ValuesAsNumpy()

        daily_data = {"date": pd.date_range(
            start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
            end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = daily.Interval()),
            inclusive = "left"
        )}
        daily_data["weather_code"] = daily_weather_code
        daily_data["temperature_2m_max"] = daily_temperature_2m_max
        daily_data["temperature_2m_min"] = daily_temperature_2m_min
        daily_data["sunshine_duration"] = daily_sunshine_duration
        daily_dataframe = pd.DataFrame(data = daily_data)
        return daily_dataframe


    async def getForecast(self, latitude :float, longitude:float ) -> Tuple[dict, str]:
        params = buildForecastQueryParams(latitude, longitude)
        responses = await self.getResponsesFromClient(self._url, params)
        response = responses[0]
        daily_dataframe = await self.parseResponseToDailyDict(response)
        return daily_dataframe.to_dict('list')
