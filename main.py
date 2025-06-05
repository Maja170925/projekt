

toll_both : list = [

    {'name' : 'SPO Olszowa', 'location' : 'Olszowa'},
    {'name' : 'SPO Nogowczyce', 'location' : 'Nogowczyce'},
    {'name' : 'SPO Łany', 'location' : 'Łany'},
    {'name' : 'SPO Ostropa', 'location' : 'Ostropa'},
]

def get_both_info(both_data : list) -> None:
    for both in both_data:
        print(f'{both['name']} : {both["location"]}')

get_both_info(toll_both)