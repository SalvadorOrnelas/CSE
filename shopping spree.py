shopping_spree = {
    'CENTEROFMALL': {
        'NAME': "center of mall",
        'DESCRIPTION': "you are in the center of the mall there are 4 paths going west, north, south, east",
        'PATHS': {
             'NORTH': 'OUTSIDE',
             'SOUTH': 'TILLYS',
             'EAST': 'EXPRESS',
             'WEST': 'HOLLISTERCO',

         }
    },
    'HOLLISTERCO':{
        'NAME': "Hollister Co",
        'DESCRIPTION':"your in the store. Store is filled with cloths. East and west there are doors",
        'PATHS':{
            'WEST': 'SHIEKS',
            'EAST': 'CENTEROFMALL'
        }
    },
    ''
}