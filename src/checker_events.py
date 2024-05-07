from src.constants import *


class CheckerEvents:

    def check_event(self, my_string, now_index, mistakes, event):
        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
            if (65 <= ord(my_string[now_index]) <= 90):
                if (event.key == comands_letter[ord(my_string[now_index]) - 65]):
                    now_index += 1
            elif (event.key in comands_letter) or (event.key in comands_digits):
                mistakes += 1
            elif (97 <= ord(my_string[now_index]) <= 122) and (
                    (event.key in comands_letter) or (event.key in comands_digits)):
                mistakes += 1
            elif (48 <= ord(my_string[now_index]) <= 57) and (
                    (event.key in comands_digits) or (event.key in comands_digits)):
                mistakes += 1
        elif (97 <= ord(my_string[now_index]) <= 122) and (
                event.key == comands_letter[ord(my_string[now_index]) - 97]):
            print(my_string[now_index])
            now_index += 1

        elif (48 <= ord(my_string[now_index]) <= 57) and event.key == comands_digits[
            ord(my_string[now_index]) - 48]:
            print(my_string[now_index])
            now_index += 1
        elif (ord(my_string[now_index]) == 32) and event.key == pygame.K_SPACE:
            now_index += 1
        else:
            mistakes += 1
        return mistakes, now_index
