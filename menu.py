from pip._vendor.distlib.compat import raw_input


class Menu():
    '''
        Class Menu Utama
    '''

    def __init__(self,question):
        self.question = question
        self.choices = []

    def add_choice(self,choice):
        self.choices.extend(choice)

    def input(self):
        choice_list = "\n".join("    {}) {}".format(i, x.menu_name) for i, x in enumerate(self.choices, 1))
        s = """{}\n{}\n""".format(self.question, choice_list)
        prompt = "? "

        while True:
            user = raw_input(s + prompt)
            try:
                c = int(user.strip())
                choice = self.choices[c - 1]
            except (IndexError, ValueError):
                prompt = "ERROR: please input an integer in {}..{}\n? ".format(1, len(self.choices))
                continue
            return choice.on_selection(self, c - 1)
