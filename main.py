from utils.model import toll_both
from utils.controller import get_both_info, add_both_info


def main():
    print('=========MENU=========')
    print('0 - zakończ program')
    print('1 - wyświetl dane punktów poboru opłat')
    print('2 - dodaj punkt poboru opłat')
    print('=================')
    get_both_info(toll_both)
    while True:
        choice: str = input('wybierz opcję MENU: ')
        if choice == '0': break
        if choice == '1': get_both_info(toll_both)
        if choice == '2': add_both_info(toll_both)

if __name__ == '__main__':
    main()

