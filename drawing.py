import pygame
from settings import *
from ray_casting import ray_casting

class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
    
    def background(self):
        pygame.draw.rect(self.sc, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, MGREEN, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
    
    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle)
    
    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, CRED)
        self.sc.blit(render, FPS_POS)