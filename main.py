import streamlit as st
import requests

# Title
st.title("🌤️ Simple Weather App")

# Input for city name
city = st.text_input("Enter city name:", "London")

# OpenWeatherMap API key (replace with your own)
API_KEY = "your_api_key_here"
BASE_URL = "https://openweathermap.org/api"

if st.button("Get Weather"):
    if city:
        # Build URL
        url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
        
        # Get data
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            st.success(f"Weather in {city}")
            
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            desc = data['weather'][0]['description']
            wind = data['wind']['speed']
            
            st.metric("🌡️ Temperature (°C)", f"{temp} °C")
            st.metric("💧 Humidity (%)", f"{humidity}%")
            st.metric("🌬️ Wind Speed (m/s)", f"{wind}")
            st.write(f"**Condition:** {desc.capitalize()}")
        
        else:
            st.error("City not found. Please check the name.")
