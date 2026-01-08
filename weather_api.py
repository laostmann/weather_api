### Weather API Project ###

import requests

tomorrow_api_key = '<key>'

def main():
    # Get coordinates for the user input location
    lat, lon = get_coordinates()

    if lat is None or lon is None:
        return  # stop if location lookup failed
    
    # Get weather data using the coordinates
    weather = get_weather(lat, lon)

def get_coordinates():

    # Ask user for city and state input
    location = input("Enter city and state (e.g., Chicago, IL): ").strip()
    if "," in location:
        city, state = location.split(",")  # splits at the comma
        
        # removes spaces around comma and converts to lowercase for better API compatibility
        city = city.strip().lower() 
        state = state.strip().lower() 
    else:
        print("Please enter in format: City, State")
        return None, None
    
    # Use Nominatim API to get coordinates for the city and state
    url = f'https://nominatim.openstreetmap.org/search?q={city}+{state}&format=jsonv2'
    
    headers = {"User-Agent": "my-weather-app"}
    coordinates = requests.get(url, headers=headers)
    data = coordinates.json()
    lat = data[0]['lat']
    lon = data[0]['lon']

    if not data:
        print("Location not found! Please double your check input.")
    return lat, lon

# Function to get weather data from Tomorrow API using lat and lon
def get_weather(lat, lon):
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={lat},{lon}&units=imperial&apikey={tomorrow_api_key}"
    headers = {"User-Agent": "my-weather-app", "Accept": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        temperature = data['data']['values']['temperature']
        humidity = data['data']['values']['humidity']
        uv_index = data['data']['values']['uvIndex']
        wind_gust = data['data']['values']['windGust']
        wind_speed = data['data']['values']['windSpeed']
        print(f"Temperature: {temperature}°F")
        print(f"Humidity: {humidity}%")
        print(f"UV Index: {uv_index}")
        print(f"Wind Gust: {wind_gust} mph")
        print(f"Wind Speed: {wind_speed} mph")

main()

### DONE: Feed lat, lon to tomorrow api endpoint and get data

### TODO: Add for/while loop to get multiple locations data