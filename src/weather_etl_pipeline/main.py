import os
import requests
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime


# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city: str, units: str = "metric") -> dict:
    """Obtiene datos del clima para una ciudad específica."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": units,
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al obtener datos: {response.status_code} - {response.text}")



def transform_weather_data(raw_data: dict) -> pd.DataFrame:
    """Transforms raw weather JSON into a clean Pandas DataFrame."""
    transformed = {
        "city": raw_data["name"],
        "country": raw_data["sys"]["country"],
        "temperature": raw_data["main"]["temp"],
        "humidity": raw_data["main"]["humidity"],
        "pressure": raw_data["main"]["pressure"],
        "weather_main": raw_data["weather"][0]["main"],
        "weather_description": raw_data["weather"][0]["description"],
        "wind_speed": raw_data["wind"]["speed"],
        "timestamp": datetime.utcfromtimestamp(raw_data["dt"]),
    }

    return pd.DataFrame([transformed])


def save_to_parquet(df: pd.DataFrame, output_dir: str = "data") -> str:
    """Saves the transformed weather data to a Parquet file."""
    os.makedirs(output_dir, exist_ok=True)

    timestamp_str = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"weather_{timestamp_str}.parquet"
    filepath = os.path.join(output_dir, filename)

    df.to_parquet(filepath, index=False)
    print(f"Data saved to {filepath}")
    return filepath

if __name__ == "__main__":
    city = "Bogota"
    raw = get_weather_data(city)
    df = transform_weather_data(raw)
    print("Transformed weather data:")
    print(df)
    save_to_parquet(df)