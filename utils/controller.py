def get_both_info(both_data : list) -> None:
    for both in both_data:
        print(f'{both['name']} : {both["location"]}')


def add_both_info(both_data : list) -> None:
    new_name: str = input('Podaj nazwę punktu poboru opłat')
    new_location: str = input('Podaj lokalizację punktu poboru opłat')
    both_data.append({'name': new_name, 'location': new_location})
