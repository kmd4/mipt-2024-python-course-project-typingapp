import pygame

pygame.init()
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
