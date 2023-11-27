import folium
from bs4 import BeautifulSoup
import requests
import folium

def add_user_to(users_list: list) -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('podaj imie ?')
    posts = input('podaj liczbe postow ?')
    city = input('podaj miasto')
    users_list.append({'name': name, 'posts': posts, "city": city})


def remove_user_from(users_list: list) -> None:
    """
    remove object from list
    :param users_list: list - user list
    :return: None
    """

    tap_list = []
    name = input('podaj imie uzytkownika do usuniecia')
    for user in users_list:
        if user['name'] == name:
            tap_list.append(user)
    print('Znaleziono uzytkownikow :')
    print('0: Usun wszystkich zmienionych uzytkownikow')
    for numerek, user_to_be_removed in enumerate(tap_list):
        print(f'{numerek + 1}: {user_to_be_removed}')
    numer = int(input(f'Wybierz uzytkownika do usuniecia'))
    if numer == 0:
        for user in tap_list:
            users_list.remove(user)
    else:
        users_list.remove(tap_list[numer - 1])


def show_users_from(users_list: list) -> None:
    for user in users_list:
        print(f'Twój znajomy {user["name"]} dodał {user["posts"]}')


def gui(users_list, user_list=None) -> None:
    while True:
        print(f'MENU'
              f'Wyjdź\n'
              f'1: Wyświetl użytkowników\n'
              f'2: Dodaj użytkownika\n'
              f'3: Usuń użytkownika\n'
              f'4: Modyfikuj użytkownika\n'
              f'5:Wygeneruj mapę z użytkownikiem\n'
              f'6:Wygeneruj mapę z użytkownikami ')

        menu_option = input('Podaj funkcje do wywołania')
        print(f'Wybrane funkcje {menu_option}')

        match menu_option:
            case '0':
                print('Kończę prace')
            case '1':
                print('Wyświetl nazwę użytkownika')
                show_users_from(users_list)
            case '2':
                print('Dodaj użytkownika')
                add_user_to(users_list)
            case '3':
                print('Usuwam użytkownika')
                remove_user_from(users_list)
            case '4':
                print('Modyfikuj uzytkownika')
                update_user(users_list)
            case '5':
                print('Rysuj mapę z użytkownikiem')
                user = input('podaj nazwe użytkownika do modyfikacji')
                for item in users_list:
                    if item['nick']== user:
                        get_single_map_of(item)
            case '6':
                print('Rysuj mapę z wszytkimi użytkownikami ')
                get_map_of(users_list)


nazwy_miejscowosci = ['Opoczno', 'Lublin', 'Ślipcze', 'Czumów', 'Berlin']


def get_cooordinate_of(city: str) -> list[float, float]:
    # pobranie strony internetowej

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'
    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')

    # pobranie współrzędnych z treści strony internetowej

    response_html_latitude = response_html.select('.latitude')[1].text  # . ponieważ class
    response_html_latitude = float(response_html_latitude.replace(',', '.'))

    response_html_longitude = response_html.select('.longitude')[1].text  # . ponieważ class
    response_html_longitude = float(response_html_longitude.replace(',', '.'))

    return [response_html_latitude, response_html_longitude]


# for item in nazwy_miejscowosci:
# print(get_cooordinate_of(item))


# from .dane import users_list

# Zwrócić mape z pinezką odnoszącą się do wskaznego na podstawie nazwy użytkownika podanej z klawiatury
user = {"city": "Zamość", "name": "Kasia", "nick": "katarzyna", "posts": 32323},


# Zwróci mapę z wszystkimi użytkownikami z danej listy
##Rysowanie mapy
def get_single_map_of(user: str) -> None:
    city = get_cooordinate_of(user['city'])
    map = folium.Map(
        location=city,
        tiles='OpenStreetMap',
        zoom_start=14, )
    folium.Marker(
        location=city,
        popup=f'Tu rządzi {user["name"]} z GEOINFORMATYKi 2023 \n OU YEAH!!!💃'
    ).add_to(map)
    map.save(f'mapka_{user["name"]}.html')


def get_map_of(users: list[dict, dict]) -> None:
    map = folium.Map(
        location=[52.3, 21.8],
        tiles='OpenStreetMap',
        zoom_start=14, )
    for user in users:
        folium.Marker(
            location=get_cooordinate_of(city=user['city']),
            popup=f'Użytkownik: {user["name"]}\n'
                  f'Liczba postów {user["posts"]}'
        ).add_to(map)
        map.save(f'mapka.html')
def update_user(users_list: list[dict, dict]) -> None:
    nick_of_user = input("Podaj nick użytkownika do modyfikacji:")
    print(nick_of_user)
    for user in users_list:
        if user["nick"] == nick_of_user:
            print("Znaleziono !!!")
            user['name'] = input("Podaj nowe imię: ")
            user['nick'] = input("Podaj nowA ksywkę: ")
            user['posts'] = int(input("Podaj liczbę postów: "))
            user['city'] = int(input("Podaj miasto:"))
