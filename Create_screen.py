import pygame

from tools.Load_music import load_music
from tools.Load_image import load_image


def create_screen():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Клавиатурный тренажер')
    pygame.display.set_icon(load_image('play-button.png'))
    load_music("Hello.mp3").play()
    pygame.display.flip()
    return screen;