from src.buttons import *
from src.create_screen import width, height


def draw_level(screen, now_index, my_str, mistakes, ticks, pause_flag):
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 24)
    time = '{minutes:02d}:{seconds:02d}'.format(minutes=minutes, seconds=seconds)

    screen.fill((0, 0, 0))

    font = pygame.font.Font("fonts/introheadr-base.ttf", 40)
    font1 = pygame.font.Font("fonts/introrustg-base2line.ttf", 20)
    text_all = font.render(my_str, True, (100, 255, 100))
    text_written = font.render(my_str[:now_index], True, (100, 255, 100))
    text_unwritten = font.render(my_str[now_index:], True, (100, 100, 100))
    text_mistakes = font1.render(f"Mistakes: {mistakes}", True, (100, 255, 100))
    text_time = font1.render(time, True, (100, 255, 100))

    all_text_x = width // 2 - text_all.get_width() // 2
    all_text_y = height // 2 - text_all.get_height() // 2

    text_unwritten_x = width // 2 - text_all.get_width() // 2 + text_written.get_width()
    text_unwritten_y = height // 2 - text_all.get_height() // 2

    text_mistakes_x = 140
    text_mistakes_y = 25

    text_time_x = screen.get_width() - 20 - text_time.get_width()
    text_time_y = 20

    text_w = text_all.get_width()
    text_h = text_all.get_height()

    screen.blit(text_written, (all_text_x, all_text_y))
    screen.blit(text_unwritten, (text_unwritten_x, text_unwritten_y))
    screen.blit(text_mistakes, (text_mistakes_x, text_mistakes_y))
    screen.blit(text_time, (text_time_x, text_time_y))

    pygame.draw.rect(screen, (0, 255, 0), (all_text_x - 10, all_text_y - 10,
                                           text_w + 20, text_h + 20), 1)
    if pause_flag:
        draw_pause(screen)


def draw_start_page(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("fonts/introrustg-base2line.ttf", 40)
    text = font.render("Клавиатурный тренажер", True, (255, 255, 255))

    all_text_x = width // 2 - text.get_width() // 2
    all_text_y = height // 2 - text.get_height() // 2 - 50

    screen.blit(text, (all_text_x, all_text_y))


def draw_pause(screen):
    font = pygame.font.Font("fonts/introrustg-base2line.ttf", 40)
    text_pause = font.render("Pause", True, (255, 255, 255))

    text_pause_x = width // 2 - text_pause.get_width() // 2
    text_pause_y = height // 2 - text_pause.get_height() // 2 - 100

    screen.blit(text_pause, (text_pause_x, text_pause_y))


def draw_game_over(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font("fonts/introrustg-base2line.ttf", 40)
    text_game_over = font.render("Game over", True, (255, 255, 255))

    text_game_over_x = width // 2 - text_game_over.get_width() // 2
    text_game_over_y = height // 2 - text_game_over.get_height() // 2

    screen.blit(text_game_over, (text_game_over_x, text_game_over_y))
