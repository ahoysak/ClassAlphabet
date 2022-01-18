from function_alpha import *

print('Select language')
while True:
    print('1. English alphabet\n'
           + '2. Ukrainian alphabet')

    select_choose = int(input('Select a language: ')) #вибір команди
    if select_choose == 1:
        print('Choose an action with the English alphabet: \n'
               + '1. Number of letters\n' #кількість букв
               + '2. Check letter\n'      #перевірити чи до англ алфавіту належить
               + '3. Example text in English ')  #приклад англ мовою
        next_select_choose = int(input('Your choose: '))
        if next_select_choose == 1:
            english = alphabet()
            english.eng_lens()
        elif next_select_choose == 2:
            english = alphabet()
            english.check_lettereng()
        elif next_select_choose == 3:
            english = alphabet()
            english.eng_text()


    elif select_choose == 2:
        print('Choose an action with the Ukrainian alphabet: \n'
              + '1.Надрукувати алфавіт\n'
              + '2. Порахувати кількість букв')
        nextt_select_choose = int(input('Ваш вибір: '))
        if nextt_select_choose == 1:
            ukrainian = alphabett()
            ukrainian.ukr_alph()
        elif next_select_choose == 2:
            ukrainian = alphabett()
            ukrainian.ukr_lens()