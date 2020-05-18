import pygame
import os 
import time 
import random 

#sey up py game window 
WIDTH, HEIGHT = 750,750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space invader")

#laod images 
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
#if you want to load a folder name from the file name you can os.path,join
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

#player ship 
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

#lasers 
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#background
BG = pygame.image.load(os.path.join("assets", "background-black.png"))

