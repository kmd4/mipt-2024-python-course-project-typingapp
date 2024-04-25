import os

import pygame


def load_music(name):
    fullname = os.path.join("musics", name)
    try:
        return pygame.mixer.Sound(fullname)
    except pygame.error as ex:
        print("Cant load music {} because: {}".format(name, ex))