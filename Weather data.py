import requests

# Specify the city and country code
city = "Kolkata"
country = "IN"

# Replace with your OpenWeatherMap API key
api_key = "your_actual_api_key"

# Construct the API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Weather Data for Kolkata, India:", data)
else:
    print("Error:", response.status_code, response.json())
