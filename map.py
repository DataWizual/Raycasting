from settings import *

text_map = [
    'WWWWWWWWWWWW',
    'W..........W',
    'W...WWWW...W',
    'W......W...W',
    'W..........W',
    'W..WWWWW...W',
    'W..........W',
    'WWWWWWWWWWWW'    
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))