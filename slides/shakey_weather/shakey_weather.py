import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=imperial"  # Units are in Fahrenheit
    response = requests.get(complete_url)
    data = response.json()
    
    # Print the raw response for debugging
    print(data)

    # Check if the API responded with valid data
    if data.get("cod") == 200:  # 200 indicates a successful request
        main_data = data.get("main", {})
        weather_data = data.get("weather", [{}])[0]

        # Retrieve values safely with get() in case any keys are missing
        temp = main_data.get("temp", "N/A")
        pressure = main_data.get("pressure", "N/A")
        humidity = main_data.get("humidity", "N/A")
        description = weather_data.get("description", "N/A")
        
        print(f"Temperature: {temp}°F")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {description}")
    else:
        print(f"Error: Unable to get weather data for {city_name}. Reason: {data.get('message', 'Unknown error')}")

if __name__ == "__main__":
    api_key = "4df8c8bb3a112b3f697a9202993bbbba"  # Make sure to use a valid API key
    city = input("Enter the city name: ")
    
    # Get the weather report
    weather_report = get_weather(city, api_key)
    
    # Print the weather report to the command line
    print(weather_report)
