import math
import datetime
import requests
from langchain_core.tools import tool
from pydantic import BaseModel, Field

# PYDANTIC SCHEMAS (Strict Inputs)
# This tells the LLM: "If you use the calculator, you MUST provide a string called 'expression'."
class CalculatorInput(BaseModel):
    expression: str = Field(description="The mathematical expression to evaluate, e.g., '2 + 2' or '15/100 * 240'")

class WeatherInput(BaseModel):
    city: str = Field(description="The name of the city, e.g., 'London' or 'Tokyo'")

# Calculator tool
@tool("calculator", args_schema=CalculatorInput)
def calculate(expression: str) -> str:
    """Use this tool to evaluate mathematical expressions. Input must be a valid Python math string."""
    try:
        # Safe evaluation of math
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names.update({"abs": abs, "round": round})
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Error calculating: {str(e)}"

# Datetime tool
@tool
def get_current_datetime() -> str:
    """Use this tool to get the current date and time. Do not guess the date; always use this tool when the user asks for 'today' or 'now'."""
    now = datetime.datetime.now()
    return now.strftime("%A, %B %d, %Y, %I:%M %p")

# Weather tool
@tool("get_weather", args_schema=WeatherInput)
def get_weather(city: str) -> str:
    """Use this tool to get the current weather for a specific location. 
       The location can be a city, a state, or a country (e.g., 'London', 'Malaysia', 'New York')."""
    try:
        # Step A: Geocoding
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geo_res = requests.get(geo_url).json()
        
        if not geo_res.get("results"):
            return f"Could not find weather data for city: {city}"
            
        location = geo_res["results"][0]
        lat, lon = location["latitude"], location["longitude"]
        country = location.get("country", "")
        
        # Step B: Fetch weather
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_res = requests.get(weather_url).json()
        
        current = weather_res.get("current_weather", {})
        temp = current.get("temperature")
        wind = current.get("windspeed")
        
        return f"The current weather in {city}, {country} is {temp}°C with a wind speed of {wind} km/h."
        
    except Exception as e:
        return f"Error fetching weather: {str(e)}"