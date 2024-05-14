# Imports!
import math
import random
import pygame
from pygame import mixer

# Initialise pygame!
pygame.init()
screen = pygame.display.set_mode((800, 500)) # Create screen!

# Background shennanigans!
background = pygame.image.load('background.png')

# Sound shennanigans!
# I haven't found a proper background audio yet.
#mixer.music.load("background.wav")
#mixer.music.play(-1)

# Window Title & Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)