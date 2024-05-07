from src.constants import *


class Button:
    def __init__(self, x, y, width, height, image, hover_image=None, sound=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if (hover_image is not None):
            self.hover_image = pygame.image.load(hover_image)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound:
            self.sound = pygame.mixer.Sound(sound)

    def draw(self, screen):
        current_image = self.image
        if self.hovered:
            current_image = self.hover_image

        screen.blit(current_image, self.rect.topleft)

    def check_hover(self, mouse_position):
        self.hovered = self.rect.collidepoint(mouse_position)

    def execute_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
            return True
        return False


start_game_button = Button(width / 2 - 100, 300, 200, 60, "images/play.png", "images/play_hover.png",
                           "musics/click.mp3")
pause_button = Button(70, 10, 50, 50, "images/pause.png", "images/pause_hover.png", "musics/click.mp3")
menu_button = Button(10, 10, 50, 50, "images/menu.png", "images/menu_hover.png", "musics/click.mp3")
restart_button = Button(width / 2 - 25, 350, 50, 50, "images/restart.png", "images/restart_hover.png",
                        "musics/click.mp3")
