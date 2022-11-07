import json
import requests


def string_to_float(convertable_object):
    i = 0
    cut_string = convertable_object
    list_of_degrees = []
    while i < len(cut_string):
        if cut_string[i].isdigit() or cut_string[i] == ".":
            only_necessary = cut_string[i]
            list_of_degrees.append(only_necessary)
        i += 1
    convertable_string = ' '.join(list_of_degrees)
    spaces_removed = convertable_string.replace(" ", "")
    degrees_in_float = float(spaces_removed)
    return degrees_in_float


def get_latitude(place):
    geo_codes = (f"http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=2&appid={api_key}")
    data = requests.get(geo_codes).json()
    get_lat_formatted = json.dumps(data)
    index_of_lat = get_lat_formatted.find('"lat":')
    lat_ends_index = get_lat_formatted.find(' "lon": ')
    cut_string = get_lat_formatted[index_of_lat:lat_ends_index]
    latitude = string_to_float(cut_string)
    return latitude


def get_longitude(place):
    geo_codes = (f"http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=2&appid={api_key}")
    data = requests.get(geo_codes).json()
    get_lon_formatted = json.dumps(data)
    index_of_lon = get_lon_formatted.find('"lon":')
    lon_ends_index = get_lon_formatted.find(' "country":')
    cut_string = get_lon_formatted[index_of_lon:lon_ends_index]
    longitude = string_to_float(cut_string)
    return longitude


def get_the_weather(lat, lon):
    get_places_weather = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
    weather = requests.get(get_places_weather).json()
    degrees = weather["main"]["temp"]
    celcius = degrees
    return round(celcius, 2)

userInput = input("Kirjoita kaupungin nimi: ")
while userInput != "":
    api_key = ("af4fe2ce6320a671dfd8ff76e98ff081")
    latitude = get_latitude(userInput)
    longitude = get_longitude(userInput)
    celcius = get_the_weather(latitude, longitude)
    print(f"Kaupungissa {userInput} lämpotila on {celcius} C\u00B0")
    userInput = input("Kirjoita kaupungin nimi: ")