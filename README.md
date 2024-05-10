<h1 align="center">
Weather (and Energy) Forecast API
</h1>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#run">Run</a> •
  <a href="#endpoints">Endpoints</a>  
</p>

# Description 
An application to display the weather forecast for the next 7 days using an external API. Additionally, the application should estimate the forecasted energy production from a photovoltaic installation.

# Run 
### From repository
```cmd
git clone https://github.com/kamiderka/weather-forecast-api.git
cd weather-forecast-api
pip install -r requirements.txt
fastapi run src/main.py
```
### From Dockerfile
```cmd
git clone https://github.com/kamiderka/weather-forecast-api.git
cd weather-forecast-api
docker build -t toringen/weather-forecast-api:latest .
docker run -p 8080:8080  toringen/weather-forecast-api:latest
```

### Pull image from DockerHub
```cmd
docker pull toringen/weather-forecast-api:latest
docker run -p 8080:8080  toringen/weather-forecast-api:latest
```
or...
you can contact me to get URL to my **Azure deployment**

# Endpoints
Unfortunately there is only one (but still amazing) endpoint:  

## GET /forecast
Get the weather forecast and estimate energy production from a photovoltaic installation for the next 7 days based on specified latitude and longitude coordinates.

**Parameters**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `latitude` | required | float  | Supported values: `<-90.0;90.0>`                                                                                                                                           |
|     `longitude` | required | float  | Supported values: `<-180.0;180.0>`                                                                                                                                           |

**Response**

```json
{
    "date": [
        "2024-05-10T00:00:00+00:00",
        "2024-05-11T00:00:00+00:00",
        "2024-05-12T00:00:00+00:00",
        "2024-05-13T00:00:00+00:00",
        "2024-05-14T00:00:00+00:00",
        "2024-05-15T00:00:00+00:00",
        "2024-05-16T00:00:00+00:00"
    ],
    "weather_code": [
        3.0,
        80.0,
        3.0,
        3.0,
        2.0,
        2.0,
        3.0
    ],
    "temperature_2m_max": [
        42.002498626708984,
        40.95249938964844,
        39.40250015258789,
        42.252498626708984,
        44.0525016784668,
        42.852500915527344,
        41.90250015258789
    ],
    "temperature_2m_min": [
        31.15250015258789,
        30.702499389648438,
        29.90250015258789,
        29.40250015258789,
        29.852500915527344,
        30.452499389648438,
        30.252500534057617
    ],
    "sunshine_duration": [
        42799.9140625,
        35614.44921875,
        38071.3359375,
        43126.1640625,
        43144.61328125,
        42643.05859375,
        43088.17578125
    ],
    "energy": [
        5.944432508680555,
        4.946451280381944,
        5.287685546875,
        5.989745008680556,
        5.992307400173611,
        5.922647026909722,
        5.984468858506944
    ]
}
```
or
```json
{
    "detail": "Latitude should be in range <-90°:90°>. Given: 1223.0"
}
```
