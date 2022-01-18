class alphabet:
    eng = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
           "X",
           "Y", "Z"]

    def eng_lens(self):
        print(len(self.eng))

    def eng_text(self):
        print('This is simple text for Lubomir')

    def check_lettereng(self):
        print('WARNING! the letter must be uppercase')
        letter = input('Your letter: ')
        if letter in self.eng:
            print('Yes.')
        else:
            print('No')



class alphabett:
    ukr = ["А","Б","В","Г","Г","Д","Е","Є","Ж","З","І","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Щ","Ш","Ю"]

    def ukr_alph(self):
        print(self.ukr)

    def ukr_lens(self):
        print(len(self.ukr))
