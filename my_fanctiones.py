def add_user_to(users_list: list) -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('podaj imie ?')
    posts = input('podaj liczbe postow ?')
    users_list.append({'name':name, 'posts': posts})

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
        for user in tap_list:
            users_list.remove(user)
    else:
        users_list.remove(tap_list[numer-1])


def show_users_from(users_list:list)  -> None:
    for user in users_list:
        print(f'Twój znajomy {user["name"]} dodał {user["posts"]}')



def gui()-> None:
    while True:
     print(f'MENU'
      f'Wyjdź\n'
      f'1: Wyświetl użytkowników\n'
      f'2: Dodaj użytkownika\n'
      f'3: Usuń użytkownika\n'
      f'4: Modyfikuj użytkownika\n')

    menu_option = input('Podaj funkcje do wywołania')
    print(f'Wybrane funkcje {menu_option}')

    match menu_option:
        case '0':
            print('Kończę prace')
            break
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
            print('to bedzie zrobione') #TODO add rhis function to my function

gui()