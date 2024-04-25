import sys
from Create_screen import *
from Scenes import *


def main():
    pygame.init()
    screen = create_screen()
    start_menu(screen)
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())