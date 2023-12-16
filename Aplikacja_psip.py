import psycopg2
from dane import users_list

db_params = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='Psip_2023',
    host='localhost',
    port=5432
)

cursor = db_params.cursor()

# Dodajemy użytkownika do tabeli
def dodaj_uzytkownika(user: str):
    for nick in users_list:
        if user == nick['nick']:
            sql_query_1 = f"INSERT INTO public.aplikacjon(city, name, nick, posts) VALUES('{nick['city']}', '{nick['name']}', '{nick['nick']}', {nick['posts']});"
            cursor.execute(sql_query_1)
            db_params.commit()

dodaj_uzytkownika(input('podaj nick'))
