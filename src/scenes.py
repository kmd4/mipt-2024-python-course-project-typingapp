from src.checker_events import *
from src.drawing import *


def start_menu(screen):
    draw_start_page(screen)
    running = True

    while running:
        for event in pygame.event.get():
            # if event.type == pygame.MOUSEBUTTONDOWN and start_button.rect.collidepoint(event.pos):
            #     start_button.clicked(screen)
            if event.type == pygame.QUIT:
                running = False
            if start_game_button.execute_event(event):
                start_level(screen, 1, 0, pygame.time.get_ticks())
        draw_start_page(screen)
        start_game_button.check_hover(pygame.mouse.get_pos())
        start_game_button.draw(screen)
        pygame.display.flip()
    pygame.quit()


def start_level(screen, number_level, mistakes, start_time):
    f_level = open(f"levels/level_{number_level}", 'r')
    pause_flag = False
    my_string = f_level.readline().strip()
    size_string = len(my_string)
    now_index = 0
    checker = CheckerEvents()
    pause_time = 0
    start_pause_time = 0
    end_pause_time = 0

    ticks = pygame.time.get_ticks() - start_time;
    draw_level(screen, now_index, my_string, mistakes, ticks, pause_flag)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and not pause_flag and now_index < size_string:
                mistakes, now_index = checker.check_event(my_string, now_index, mistakes, event)
            if event.type == pygame.QUIT:
                running = False
            if menu_button.execute_event(event):
                start_menu(screen)
            if pause_button.execute_event(event):
                if not pause_flag:
                    pause_flag = True
                    start_pause_time = pygame.time.get_ticks()
                else:
                    pause_flag = False
                    end_pause_time = pygame.time.get_ticks()
                    pause_time += end_pause_time - start_pause_time
        if mistakes > 9 or (pygame.time.get_ticks() - start_time - pause_time) > 600000:
            game_over(screen)
        if not pause_flag:
            ticks = pygame.time.get_ticks() - start_time - pause_time
        draw_level(screen, now_index, my_string, mistakes, ticks, pause_flag)
        if now_index == size_string:
            for i in range(1000000):
                pass
            start_level(screen, max(1, (number_level + 1) % 7), mistakes, pygame.time.get_ticks())
        menu_button.check_hover(pygame.mouse.get_pos())
        menu_button.draw(screen)
        pause_button.check_hover(pygame.mouse.get_pos())
        pause_button.draw(screen)
        pygame.display.flip()
    pygame.quit()


def game_over(screen):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if restart_button.execute_event(event):
                start_menu(screen)
        draw_game_over(screen)
        restart_button.check_hover(pygame.mouse.get_pos())
        restart_button.draw(screen)
        pygame.display.flip()
    pygame.quit()
