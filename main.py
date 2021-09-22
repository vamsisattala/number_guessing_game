import random
print('''
    welcome to number guessing game 
''')
actual_number = random.randint(1,100)
def game(parm):
    attempts = parm
    print(f'you have {attempts} attempts')
    for i in range(attempts):
        attempts -= 1
        gussed_number = int(input('enter your guessed number: '))
        if gussed_number > actual_number:
            print('too high')
            print(f'you have {attempts} attempts left')
        elif gussed_number < actual_number:
            print('too low')
            print(f'you have {attempts} attempts left')
        elif gussed_number == actual_number:
            print(f'congratulations man!! you won the match with {attempts} attempts left')
            exit()
        else:
            print('looser...you failed the match')

#ask user to play
choice = input('chose your level of difficulty "easy" or "hard" :')

if choice == 'easy':
    game(10)
else:
    game(5)
