import pygame

class Checker_events:
    def __init__(self):
        self.comands_letter = [pygame.K_a,
                          pygame.K_b,
                          pygame.K_c,
                          pygame.K_d,
                          pygame.K_e,
                          pygame.K_f,
                          pygame.K_g,
                          pygame.K_h,
                          pygame.K_i,
                          pygame.K_j,
                          pygame.K_k,
                          pygame.K_l,
                          pygame.K_m,
                          pygame.K_n,
                          pygame.K_o,
                          pygame.K_p,
                          pygame.K_q,
                          pygame.K_r,
                          pygame.K_s,
                          pygame.K_t,
                          pygame.K_u,
                          pygame.K_v,
                          pygame.K_w,
                          pygame.K_x,
                          pygame.K_y,
                          pygame.K_z]

        self.comands_digits = [pygame.K_0,
                          pygame.K_1,
                          pygame.K_2,
                          pygame.K_3,
                          pygame.K_4,
                          pygame.K_5,
                          pygame.K_6,
                          pygame.K_7,
                          pygame.K_8,
                          pygame.K_9]

    def check_event(self, my_string, now_index, mistakes, event):
        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
            if (65 <= ord(my_string[now_index]) <= 90):
                if (event.key == self.comands_letter[ord(my_string[now_index]) - 65]):
                    print("SHIFT + ", my_string[now_index])
                    now_index += 1
            elif (event.key in self.comands_letter) or (event.key in self.comands_digits):
                mistakes += 1
                print("ER")
            elif (97 <= ord(my_string[now_index]) <= 122) and ((event.key in self.comands_letter) or (event.key in self.comands_digits)):
                mistakes += 1
                print("ERROR!")
            elif (48 <= ord(my_string[now_index]) <= 57) and ((event.key in self.comands_digits) or (event.key in self.comands_digits)):
                mistakes += 1
                print("ERROR!")
        elif (97 <= ord(my_string[now_index]) <= 122) and (event.key == self.comands_letter[ord(my_string[now_index]) - 97]):
            print(my_string[now_index])
            now_index += 1

        elif (48 <= ord(my_string[now_index]) <= 57) and event.key == self.comands_digits[ord(my_string[now_index]) - 48]:
            print(my_string[now_index])
            now_index += 1
        elif (ord(my_string[now_index]) == 32) and event.key == pygame.K_SPACE:
            print("space")
            now_index += 1
        else:
            mistakes += 1
            print("ERORRRR!!")
        return mistakes, now_index
