import sys
from src.Create_screen import *
from src.Scenes import *


def main():
    pygame.init()
    screen = create_screen()
    start_menu(screen)
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())