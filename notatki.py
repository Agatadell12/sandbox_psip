from bs4 import BeautifulSoup
import requests
import re
import folium

#pobranie strony internetowej

nazwy_miejscowosci = ['Opoczno', 'Lublin', 'Ślipcze', 'Czumów', 'Berlin']
def get_cooordinate_of(city:str)->list[float,float]:
    # pobranie strony internetowej

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'
    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')

    # pobranie współrzędnych z treści strony internetowej

    response_html_latitude = response_html.select('.latitude')[1].text  # . ponieważ class
    response_html_latitude = float(response_html_latitude.replace(',', '.'))

    response_html_longitude = response_html.select('.longitude')[1].text  # . ponieważ class
    response_html_longitude = float(response_html_longitude.replace(',', '.'))

    return[response_html_latitude, response_html_longitude]
#for item in nazwy_miejscowosci:
    #print(get_cooordinate_of(item))


#from .dane import users_list

#Zwrócić mape z pinezką odnoszącą się do wskaznego na podstawie nazwy użytkownika podanej z klawiatury
user = {"city": "Zamość", "name": "Kasia", "nick": "katarzyna", "posts": 32323},
#Zwróci mapę z wszystkimi użytkownikami z danej listy
##Rysowanie mapy
def get_single_map_of(user: str) -> None:
    city = get_cooordinate_of(user['city'])
    map = folium.Map(
        location=city,
        tiles='OpenStreetMap',
        zoom_start=14,)
    folium.Marker(
        location=city,
        popup=f'Tu rządzi {user["name"]} z GEOINFORMATYKi 2023 \n OU YEAH!!!💃'
    ).add_to(map)
    map.save(f'mapka_{user["name"]}.html')
    
def get_map_of(users: list) -> None:
    map = folium.Map(
        location=[52.3, 21.8],
        tiles='OpenStreetMap',
        zoom_start=14,)
    for user in users:
        folium.Marker(
            location=get_cooordinate_of(city=user['city']),
            popup=f'Użytkownik: {user["name"]}\n'
                  f'Liczba postów {user["posts"]}'
        ).add_to(map)
        map.save(f'mapka.html')

from dane import users_list

get_map_of(users_list)

