import openmeteo_requests

import requests_cache
import pandas as pd
from openmeteoclient import OpenMeteoClient

client = OpenMeteoClient()

print(client.getForecast(-12.323, 80.213))