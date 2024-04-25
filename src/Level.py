import os, os.path

class Level():
    def __init__(self):
        self.string = ""

    def check_string(self, string):
        print(len(string))
        if len(string) > 30:
            return "This string is too long. Input less than 30 characters."
        for (i, char) in enumerate(string):
            if not(char.isalpha() or char.isdigit() or char == " "):
                return "Infalid characters. Use only digits, spaces and letters from latin alphabet."
        return "OK"

    def get_string(self):
        new_string = input()
        checking = self.check_string(new_string)
        if checking == "OK":
            self.createLevel(new_string)
            return
        return checking

    def createLevel(self, new_string):
        lst = os.listdir("../levels")  # your directory path
        count_levels = len(lst)
        f = open(f"levels/level_{count_levels + 1}", "w")
        self.string = new_string
        f.write(new_string)
        f.close()

