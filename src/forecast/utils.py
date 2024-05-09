from typing import Tuple

PHOTOVOLTAIC_POWER = 2.5#kW
PANEL_EFFCIENCY = 0.2


def validateCoordinates(latitude :float, longitude:float) -> Tuple[bool, str]:
    if latitude < -90 or latitude > 90:
        return False, f"Latitude should be in range <-90°:90°>. Given: {latitude}"

    if longitude < -180 or longitude > 180:
        return False, f"Latitude should be in range <-180°:180°>. Given: {longitude}"

    return True, None

def buildForecastQueryParams(latitude :float, longitude:float) -> dict:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunshine_duration"]
    }
    return params

def getEnergyFromSunlightDuration(sunlight_duration :float)->float:
    return sunlight_duration*PHOTOVOLTAIC_POWER*PANEL_EFFCIENCY/3600

