import os

import pygame


def load_image(name, color_key=-1, width=None, height=None):
    pygame.init()
    fullname = os.path.join('images', name)
    try:
        if not color_key:
            image = pygame.image.load(fullname).convert_alpha()
        else:
            image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    if width != None or height != None:
        image = pygame.transform.scale(image, (width, height))
    return image
