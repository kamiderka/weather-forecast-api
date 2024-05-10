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

### GET /forecast
Get basics billing data for the current user or for a given organization ID (as long as the current user is part of that organization). (it has been poorly implemented for now to unblock the Analyze team, and should only be used by Analyze) `official client only`

**Parameters**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `latitude` | required | float  | The product for which to perform the action. <br/><br/> Supported values: `publish` or `analyze`.                                                                     |
|     `longitude` | required | float  | The organization ID for which to perform the action. <br/><br/> Default is `null`. <br/><br/> If passed, we will check if the user is part of that organization before returning any information.                                                                     |

**Response**

```json
{
    "success": true,
    "data": {
        "subscriptions": []
    }
}
```
or
```json
{
    "success": true,
    "data": {
        "subscriptions": [
            
        ]
    }
}
