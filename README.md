<h1 align="center">
Weather (and Energy) Forecast API
</h1>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#run">Run</a> •
  <a href="#endpoints">Endpoints</a>  
</p>

# Description 
An application to display the weather forecast for the next 7 days using an external API. Additionally, the application estimates the forecasted energy production from a photovoltaic installation.

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

**Query Parameters**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `latitude` | required | float  | Supported values: `<-90.0;90.0>`                                                                                                                                           |
|     `longitude` | required | float  | Supported values: `<-180.0;180.0>`                                                                                                                                           |

**Response**
```json
[
    {
        "date": "2024-05-15T00:00:00+00:00",
        "weatherCode": 80,
        "temperatureMax": 28,
        "temperatureMin": 27,
        "energy": 5.24
    },
    
]
```
or
```json
{
    "detail": "Latitude should be in range <-90°:90°>. Given: 1223.0"
}
```
