import sys
from Create_screen import *
from Scenes import *


def main():
    pygame.init()
    screen = create_screen()
    start_level(screen, 1)
    # draw_level(screen, 0, my_string, ticks, mistakes)
    # pygame.display.flip()

    # running = True
    #
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             mistakes, now_index = checker.check_event(my_string, now_index, mistakes, event)
    #         if event.type == pygame.QUIT:
    #             running = False
    #     ticks = pygame.time.get_ticks()
    #     # draw_level(screen, now_index, my_string, ticks, mistakes)
    #     draw_start_page(screen)
    #     pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())