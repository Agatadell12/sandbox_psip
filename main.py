from dane import users_list
#from utils.my_fanctiones import add_user_to, remove_user_from
#show_users_from
def gui(users_list:list)->None:
    while True:
        print( f'Menu: \n' 
            f'0: Wyjdz \n'
            f'1: Wyświetl uztkowników \n'
            f'2:Dodaj uzytkownika \n'
            f'3: Usun uzytkownika \n'
            f'4: Modyfikuj uzytkownika \n'
           )
        menu_option = input("Podaj funkcje do wywolania - ")
        print(f'Wybrano funkcje {menu_option}')

        match menu_option:
            case "0":
                print("Koncze prace")
                break
            case "1":
                print("Wyswietlam uzytkownika")
                show_users_from(users_list)
            case "2":
                print("Dodaje uzytkownika")
                add_user_to(users_list)
            case "3":
                print("Usuwam uzytkownika")
                remove_user_from(users_list)
            case "4":
                print("Usuwam uzytkownika")
                print("TODO")

gui()

