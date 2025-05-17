

import streamlit as st
import requests
import base64

def set_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background using local image
set_bg_from_local("nikolas-noonan-fQM8cbGY6iQ-unsplash.jpg")  # Make sure the file name matches your actual file



st.title("🌦️ Weather Forecast App")

# Input city name
city = st.text_input("Enter City Name")

if st.button("Get Weather"):
    if city:
        API_KEY = "b7f38265d36280fc5dc9b73a7a3987fa"  # Replace with your OpenWeatherMap API key
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description'].title()
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']

            st.subheader(f"Weather in {city.title()}")
            st.write(f"**Description:** {weather}")
            st.write(f"**Temperature:** {temp} °C")
            st.write(f"**Humidity:** {humidity}%")
            st.write(f"**Wind Speed:** {wind} m/s")
        else:
            st.error("City not found or API limit reached.")
    else:
        st.warning("Please enter a city name.")
