import sys
import pygame

from Checker_events import *
from Drawing import *
from Buttons_Sprite import *

start_game_button = pygame.sprite.Group
pause_button = pygame.sprite.Group
menu_button = pygame.sprite.Group

def start_menu(screen):

    draw_start_page(screen)


    running = True

    while running:
        for event in pygame.event.get():
            # if event.type == pygame.MOUSEBUTTONDOWN and start_button.rect.collidepoint(event.pos):
            #     start_button.clicked(screen)
            if event.type == pygame.QUIT:
                running = False
        draw_start_page(screen)
        pygame.display.flip()
    pygame.quit()


def start_level(screen, number_level):
    f_level = open(f"levels/level_{number_level}", 'r')
    my_string = f_level.readline().strip()
    now_index = 0
    mistakes = 0
    checker = Checker_events()

    ticks = pygame.time.get_ticks()
    draw_level(screen, now_index, my_string, mistakes, ticks)

    running = True

    while running:
        for event in pygame.event.get():
            # if event.type == pygame.MOUSEBUTTONDOWN and pause.rect.collidepoint(event.pos):
            #     # t = pausa.clicked()
            #     print("paused")
            # if event.type == pygame.MOUSEBUTTONDOWN and go_menu.rect.collidepoint(event.pos):
            #     running = False
            #     go_menu.clicked()
            if event.type == pygame.KEYDOWN:
                mistakes, now_index = checker.check_event(my_string, now_index, mistakes, event)
            if event.type == pygame.QUIT:
                running = False
            if mistakes > 10 or ticks / 1000 % 60 == 10:
                print("Game_Over!")
                # game_over()
        ticks = pygame.time.get_ticks()
        draw_level(screen, now_index, my_string, mistakes, ticks)
        pygame.display.flip()
    pygame.quit()