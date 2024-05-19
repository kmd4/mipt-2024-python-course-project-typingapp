import sys
from src.create_screen import *
from src.scenes import *


def main():
    pygame.init()
    screen = create_screen()
    start_menu(screen)
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
