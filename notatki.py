import sqlalchemy

db_params = sqlalchemy.URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="Psip_2023",
    host="localhost",
    database="postgres",
    port=5432
)


engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()
#sql_query_1 = aglalchemy.text("INSERT INTO public.my_table( name) VALUES('kepa');")
#sql_query_1 = sqlalchemy.text("select * from public.my_table;")
#user=input('podaj nazwe zawodnika do usuniecia')
#sql_query_1 = sqlalchemy.text("DELETE FROM public.my_table WHERE name='{user}';")
# kogo_zamienic=input('podaj kogo zmienic')
# na_kogo=input('podaj na kogo zamienic')
# sql_query_1 = sqlalchemy.text("UPDATE public.my_table SET name= {'na_kogo'} WHERE name= {'kogo_zamienic'};")

def dodaj_uzytkownika(user: str):
    sql_query_1 = sqlalchemy.text("INSERT INTO public.my_table( name) VALUES('{user}');")
    connection.execute(sql_query_1)
    connection.commit()

# cwok='staniu'
# dodaj_uzytkownika(cwok)

def usun_uzytkownika(user: str):
    sql_query_1 = sqlalchemy.text("DELETE FROM public.my_table WHERE name='{user}';")
    connection.execute(sql_query_1)
    connection.commit()

# cwok='staniu'
# usun_uzytkownika(cwok)

def aktualizuj_uzytkonika(user_1: str, user_2: str):
    sql_query_1 = sqlalchemy.text("UPDATE public.my_table SET name= {'user_1'} WHERE name= {'user_2'};")
    connection.execute(sql_query_1)
    connection.commit()

aktualizuj_uzytkonika(
    user_1=input('kogo zaminic'),
    user_2=input('na kogo zmienic'))

# connection.execute(sql_query_1)
# connection.commit()