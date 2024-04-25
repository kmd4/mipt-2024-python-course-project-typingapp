import pygame

from tools.Load_music import load_music
from tools.Load_image import load_image
size = width, height = 800, 600

def create_screen():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Клавиатурный тренажер')
    pygame.display.set_icon(load_image('icon.png'))
    load_music("Hello.mp3").play()
    pygame.display.flip()
    return screen;