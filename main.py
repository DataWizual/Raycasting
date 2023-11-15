import pygame
from settings import *
from player import Player
import math
from map import world_map
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    player.movement()
    sc.fill(BLACK)
    
    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    
    pygame.display.flip()
    clock.tick()