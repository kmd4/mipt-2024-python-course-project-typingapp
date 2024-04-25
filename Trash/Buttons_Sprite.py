from tools.Load_image import *
from src.Scenes import *

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = self.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def clicked(self):
        pass


# class Pause(Button):
#     flag_not_paused = True
#     image = load_image('7.png', color_key=-1, width=50, height=50)
#
#     def clicked(self):
#         t = get_paused(self.flag_not_paused)
#         self.flag_not_paused = not self.flag_not_paused
#         return t


# class Menu(Button):
#     image = load_image('1.png', color_key=-1, width=50, height=50)
#
#     def clicked(self):
#         from main import start
#         start()
#
#     def update(self, event):
#         if self.rect.collidepoint(event.pos):
#             self.clicked()


# class Buttons_Wins(pygame.sprite.Sprite):
#     image = load_image('None.png')
#
#     def __init__(self, x, y, *group):
#         super().__init__(*group)
#         self.rect = self.image.get_rect()
#         self.rect.x, self.rect.y = x, y


class Start(Button):
    def __init__(self, x, y):
        self.image = load_image('start.png', color_key=-1, width=50, height=50)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, event):
        if self.rect.collidepoint(event.pos):
            start_menu()


# class ReGame(Buttons_Wins):
#     image = load_image('16.png', color_key=-1, width=50, height=50)
#
#     def update(self, event):
#         if self.rect.collidepoint(event.pos):
#             from Map_Draw import start_game
#             start_game()