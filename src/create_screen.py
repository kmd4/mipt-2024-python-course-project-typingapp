import pygame

from tools.load_music import load_music
from tools.load_image import load_image
from src.constants import *


def create_screen():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Клавиатурный тренажер')
    pygame.display.set_icon(load_image('icon.png'))
    load_music("Hello.mp3").play()
    pygame.display.flip()
    return screen;
