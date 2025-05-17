# 🌤️ Weather Forecast Web App

A simple and interactive web application that displays real-time weather information for any city using **Streamlit** and the **OpenWeatherMap API**.

## 🚀 Live Demo

\[Add Live App Link Here – if deployed using Streamlit Sharing or any platform]

##

---

## 🛠️ Features

* 🌍 Get real-time weather updates for any city
* 🌡️ Displays temperature, humidity, wind speed, and weather condition
* 🧭 Easy-to-use and responsive interface
* ⚡ Built with Python and Streamlit for rapid development

---

## 📦 Tech Stack

* **Python 3**
* **Streamlit**
* **OpenWeatherMap API**

---

## 🧪 Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/weather-forecast-app.git
   cd weather-forecast-app
   ```

2. **Create and activate a virtual environment** (optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install the dependencies**

   ```bash
   pip install requests
   pip install streamlit
   pip install base64
   ```

4. **Add your OpenWeatherMap API key**

   Create a `.env` file and add:

   ```
   WEATHER_API_KEY=your_api_key_here
   ```

   Or directly paste it in the script where needed (not recommended for public repos).

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 🔑 Get an API Key

* Sign up at [https://openweathermap.org/api](https://openweathermap.org/api)
* Get your free API key to use in the app

---

## 📁 File Structure

```
weather-forecast-app/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── .env                  # API Key (not committed)
└── README.md             # Project documentation
```

---

## 🌟 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

* [Streamlit](https://streamlit.io/)
* [OpenWeatherMap](https://openweathermap.org/)
