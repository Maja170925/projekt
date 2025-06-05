from utils.model import toll_booth
from utils.controller import get_booth_info, add_booth_info, remove_booth_info, update_booth_info


def main():
    print('=========MENU=========')
    print('0 - zakończ program')
    print('1 - wyświetl dane punktów poboru opłat')
    print('2 - dodaj punkt poboru opłat')
    print('3 - usuń punkt poboru opłat')
    print('4 - zaktualizuj punkt poboru opłat')
    print('=================')
    get_booth_info(toll_booth)
    while True:
        choice: str = input('wybierz opcję MENU: ')
        if choice == '0': break
        if choice == '1': get_booth_info(toll_booth)
        if choice == '2': add_booth_info(toll_booth)
        if choice == '3': remove_booth_info(toll_booth)
        if choice == '4': update_booth_info(toll_booth)

if __name__ == '__main__':
    main()

