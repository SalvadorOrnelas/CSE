world_map = {
    'WESTHOUSE': {
        'NAME': "West of house",
        'DESCRIPTION': "You have arrived at the west of the house and there is a broken door",
        'PATH': {
            'NORTH':'NORTHOFHOUSE',
            'SOUTH':'SOUTHOFHOUSE'
        }
    },
    'NORTHHOUSE':{
        'NAME': 'north of house',
        'DESCRIPTION': "north of house",
        'PATHS': {
            'SOUTH': 'WESTOFHOUSE'
        }
    },
    'SOUTHHOUSE':{
        'NAME': 'south of house',
        'DESCRIPTION': "south of house",
        'PATHS': {
            'NORTH': 'NORTHHOUSE'
        },
    },
}

current_node = world_map['WESTHOUSE']
directions = ['NORTH', 'SOUTH','EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command =='quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map(name_of_node)
        except KeyError:
            print("you cant go that way")
    else:
        print('command not recogonized')