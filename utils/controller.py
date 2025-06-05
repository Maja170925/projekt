def get_both_info(both_data : list) -> None:
    for both in both_data:
        print(f'{both['name']} : {both["location"]}')


def add_both_info(both_data : list) -> None:
    new_name: str = input('Podaj nazwę punktu poboru opłat')
    new_location: str = input('Podaj lokalizację punktu poboru opłat')
    both_data.append({'name': new_name, 'location': new_location})

def remove_both_info(both_data : list) -> None:
    both_name: str = input('Podaj nazwę punktu poboru opłat do usunięcia')
    for both in both_data:
        if both['name'] == both_name:
            both_data.remove(both)