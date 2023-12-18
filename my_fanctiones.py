import psycopg2
from bs4 import BeautifulSoup
import requests
import folium

db_params = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='Psip_2023',
    host='localhost',
    port=5432
)

cursor = db_params.cursor()
def add_user_to() -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('Podaj imie!')
    posts = input('Podaj liczbe postow!')
    city = input('Podaj miasto!')
    nick = input('Podaj nick!')
    sql_query_1 = f"INSERT INTO public.aplikacjon(city, name, nick, posts) VALUES('{city}', '{name}', '{nick}', {posts});"
    cursor.execute(sql_query_1)
    db_params.commit()



def remove_user_from() -> None:
    """
    remove object from list
    :param users_list: list - user list
    :return: None
    """
    name = input('podaj imie uzytkownika do usuniecia')
    sql_query_1 = f"SELECT * FROM public.aplikacjon WHERE name='{name}';"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    print('Znaleziono uzytkownikow :')
    print('0: Usun wszystkich zmienionych uzytkownikow')
    for numerek, user_to_be_removed in enumerate(query_result):
        print(f'{numerek + 1}: {user_to_be_removed}')
    numer = int(input(f'Wybierz uzytkownika do usuniecia'))
    if numer == 0:
        sql_query_2 = f"DELETE * FROM public.aplikacjon;"
        cursor.execute(sql_query_2)
        db_params.commit()
    else:
        sql_query_2 = f"DELETE FROM public.aplikacjon WHERE name='{query_result[numer - 1][2]}';"
        cursor.execute(sql_query_2)
        db_params.commit()


def show_users_from() -> None:
    sql_query_1 = f"SELECT * FROM public.aplikacjon;"
    cursor.execute(sql_query_1)
    query_result=cursor.fetchall()
    for row in query_result:
        print(f'Twój znajomy {row[2]} dodał {row[4]}')

def update_user() -> None:
    nick_of_user = input("Podaj nick użytkownika do modyfikacji:")
    sql_query_1 = f"SELECT * FROM public.aplikacjon WHERE nick='{nick_of_user}';"
    cursor.execute(sql_query_1)
    print('Znaleziono')
    name = input('Podaj nowe imie: ')
    nick = input('Podaj nowe ksywke: ')
    posts = int(input('Podaj liczbe postow: '))
    city = input('Podaj nazwe miasta: ')
    sql_query_2 = f"UPDATE public.aplikacjon SET name='{name}',nick='{nick}', posts='{posts}', city='{city}' WHERE nick='{nick_of_user}';"
    cursor.execute(sql_query_2)
    db_params.commit()

# FUNKCJE MAPKI !!!


def gui() -> None:
    while True:
        print(f'MENU'
              f'0: Wyjdź\n'
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
                show_users_from()
            case '2':
                print('Dodaj użytkownika')
                add_user_to()
            case '3':
                print('Usuwam użytkownika')
                remove_user_from()
            case '4':
                print('Modyfikuj uzytkownika')
                update_user()
            case '5':
                print('Rysuj mapę z użytkownikiem')
                get_single_map_of()
            case '6':
                print('Rysuj mapę z wszytkimi użytkownikami ')
                get_map_of()


def get_cooordinate_of(city: str) -> list[float, float]:
    # pobranie strony internetowej

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'
    response = requests.get(url=adres_URL) #zwraca obiekty
    response_html = BeautifulSoup(response.text, 'html.parser')

    # pobranie współrzędnych z treści strony internetowej
    response_html_latitude = response_html.select('.latitude')[1].text  # . ponieważ class
    response_html_latitude = float(response_html_latitude.replace(',', '.'))

    response_html_longitude = response_html.select('.longitude')[1].text  # . ponieważ class
    response_html_longitude = float(response_html_longitude.replace(',', '.'))

    return [response_html_latitude, response_html_longitude]

##Rysowanie mapy
def get_single_map_of() -> None:
    city = input('Wpisz miasto uzytkownika: ')
    sql_query_1 = f"SELECT * FROM public.aplikacjon WHERE city='{city}';"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    city = get_cooordinate_of(city)
    map = folium.Map(
        location=city,
        tiles='OpenStreetMap',
        zoom_start=14, )
    for user in query_result:
        folium.Marker(
            location=city,
            popup=f'Tu rządzi {user[2]} z GEOINFORMATYKi 2023 \n'
            f'Liczba postow: {user[4]}').add_to(map)
    map.save(f'mapka_{query_result[0][1]}.html')

def get_map_of() -> None:
    map = folium.Map(
        location=[52.3, 21.8],
        tiles='OpenStreetMap',
        zoom_start=14, )
    sql_query_1 = f"SELECT * FROM public.aplikacjon;"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    for user in query_result:
        folium.Marker(
            location=get_cooordinate_of(city=user[1]),
            popup=f'Użytkownik: {user[2]}\n'
                  f'Liczba postów {user[4]}'
        ).add_to(map)
        map.save(f'mapka.html')

# POGODA ======================
def pogoda_z(miasto: str):
    url = f'https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}'
    return requests.get(url).json()
class User:
    def __init__(self, city, name, nick, posts):
        self.city = city
        self.name=name
        self.nick=nick
        self.posts=posts
    def pogoda_z(self,miasto: str):
        URL = f'https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}'
        return requests.get(URL).json()

# npc_1=User(city='warszawa', name='Agata', nick='Drzygalo', posts=123)
# npc_2=User(city='zamosc',  name='Andrew', nick='Tate', posts=888)
# print(npc_1.city)
# print(npc_2.city)
#
# print(npc_1.pogoda_z(npc_1.city))
# print(npc_2.pogoda_z(npc_2.city))
