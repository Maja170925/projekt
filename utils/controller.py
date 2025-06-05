def get_booth_info(booth_data : list) -> None:
    for booth in booth_data:
        print(f'{booth['name']} : {booth["location"]}')


def add_booth_info(booth_data : list) -> None:
    new_name: str = input('Podaj nazwę punktu poboru opłat')
    new_location: str = input('Podaj lokalizację punktu poboru opłat')
    booth_data.append({'name': new_name, 'location': new_location})

def remove_booth_info(booth_data : list) -> None:
    booth_name: str = input('Podaj nazwę punktu poboru opłat do usunięcia')
    for booth in booth_data:
        if booth['name'] == booth_name:
            booth_data.remove(booth)

def update_booth_info(booth_data : list) -> None:
    booth_name: str = input('Podaj nazwę punktu poboru opłat do aktualizacji')
    for booth in booth_data:
        if booth['name'] == booth_name:
            booth['name']=input('Podaj nową nazwę punktu poboru opłat')
            booth['location']=input('Podaj nową lokalizacje punktu poboru opłat')
