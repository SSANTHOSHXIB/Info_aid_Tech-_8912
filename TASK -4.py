import requests
from datetime import datetime

def fetch_weather_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def fetch_forecast_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]
        weather = data["weather"][0]
        description = weather["description"]
        print(f"Weather: {description}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("Location not found.")

def display_forecast(data):
    if data["cod"] != "404":
        print("Forecast for the next few days:")
        for forecast in data["list"]:
            timestamp = forecast["dt"]
            date = datetime.fromtimestamp(timestamp)
            temperature = forecast["main"]["temp"]
            description = forecast["weather"][0]["description"]
            print(f"{date.date()}: {description}, {temperature}°C")
    else:
        print("Location not found.")

def main():
    api_key = "bc104e551553851feeb1f9eb3f809f93"
    favorite_locations = []
    
    while True:
        print("\n1. Get current weather")
        print("2. Get forecast")
        print("3. Add favorite location")
        print("4. View favorite locations")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            location = input("Enter location: ")
            weather_data = fetch_weather_data(api_key, location)
            display_weather(weather_data)
        elif choice == "2":
            location = input("Enter location: ")
            forecast_data = fetch_forecast_data(api_key, location)
            display_forecast(forecast_data)
        elif choice == "3":
            location = input("Enter location to add to favorites: ")
            favorite_locations.append(location)
            print("Location added to favorites.")
        elif choice == "4":
            print("Favorite locations:")
            for loc in favorite_locations:
                print(loc)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
