import math
import datetime
import requests

#Tool 1 - Calculator
def calculate(expression:str)->str:

    """Use this tool to evaluate mathematical expressions.
       Input must be a valid Python math string, like '2 + 2' or '(15/100) * 240'."""
    
    try:
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("_")}
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

#Tool 2 - Date and Time
def get_current_datetime()->str:

    """Use this tool to get the current date and time. 
       Do not guess the date; always use this tool when the user asks for 'today' or 'now'."""
    
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

#Tool 3 - Weather Information
def get_weather(city: str) -> str:

    """Use this tool to get the current weather for a specific city.
       Input should be just the city name, like 'London' or 'Mumbai'."""
    
    try:
        # Step A: Geocoding (Turning a city name into latitude/longitude)
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geo_res = requests.get(geo_url).json()
        
        if not geo_res.get("results"):
            return f"Could not find weather data for city: {city}"
            
        location = geo_res["results"][0]
        lat, lon = location["latitude"], location["longitude"]
        country = location.get("country", "")
        
        # Step B: Fetch the weather using the coordinates
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_res = requests.get(weather_url).json()
        
        current = weather_res.get("current_weather", {})
        temp = current.get("temperature")
        wind = current.get("windspeed")
        
        return f"The current weather in {city}, {country} is {temp}°C with a wind speed of {wind} km/h."
        
    except Exception as e:
        return f"Error fetching weather: {str(e)}"
