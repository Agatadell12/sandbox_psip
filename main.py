from dane import users_list

def add_user_to(users_list: list) -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('podaj imie ?')
    posts = input('podaj liczbe postow ?')
    users_list.append({'name':name, 'posts': posts})


# add_user_to(users_list)

# mechanizm usuwania

def  remove_user_from(users_list: list) -> None:
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
        for user in users_list:
            if user['name'] == name:
                users_list.remove(user)
    else:
        users_list.remove(tap_list[numer-1])
    #print(numer)
    #print(tap_list[numer-1])
    #users_list.remove(tap_list[numer -1])




            # usuwanie znalezionego uzytkownika  z listy


remove_user_from(users_list)




# print users_list
for user in users_list:
    print(f'Twój znajomy {user["name"]} dodał {user["posts"]}')
