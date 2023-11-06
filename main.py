from dane import users_list



def add_users_to(users_list: list) -> None:
    """
    add object to list
    :param users_list: lista - user list
    :return: none
    """

    name = input('podaj imie!')
    posts =  input('podaj liczbę postów!')
    users_list.append({'name':name,'posts': posts})

add_users_to(users_list)
add_users_to(users_list)
add_users_to(users_list)


for user in users_list:
    print(f' Twój znajomy {user["name"]} dodał {user ["posts"]}')

# print(f'Twój znajmony {zmienna_na_dane[0]["nick"]} opublikował {zmienna_na_dane[0]["posts"]}')


