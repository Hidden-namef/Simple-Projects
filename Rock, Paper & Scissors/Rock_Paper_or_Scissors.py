import random

def Welcome():
    print('Welcome to the rock, paper & scissors game\n')

    while True:
        try:
            want_play = input('Do you want to play? (Yes/No): ').lower()
            if  want_play == 'yes':
                print('Ok, nice!!!\n')
                break
            elif want_play == 'no':
                print('\nOh, I see. See you later!')
                exit()
            else:
                print('\nIt is not a valid answer. Try again\n')
        except KeyboardInterrupt:
            print('Keyboard interrupt signal detected.')
            print('Exiting...')
            exit()

def Main():
    Attemps = 3
    options = ['Rock', 'Paper', 'Scissors']

    Computer_choose = random.choice(options)
    while Attemps > 0:
        while True:
            User_input = input(
                'Choose an option:\n'
                '- Rock\n'
                '- Paper\n'
                '- Scissors\n'
                'Choose: '
            ).capitalize()
            if User_input not in options:
                print('\nThis is not a valid option. Try again\n')
            else:
                print(f'\nYou have chosen: {User_input}\n')
                break

        if User_input == 'Rock' and Computer_choose == 'Paper':
            Attemps -= 1
            print(f'\nYou lost this round. You now have {Attemps} attemps\n')

        elif User_input == 'Rock' and Computer_choose == 'Scissors':
            print(f'Congratulations!!!. You win the game with {Attemps} attemps')
            exit()
        
        elif User_input == 'Scissors' and Computer_choose == 'Paper':
            print(f'Congratulations!!!. You win the game with {Attemps} attemps')
            exit()
        
        elif User_input == 'Scissors' and Computer_choose == 'Rock':
            print(f'\nYou lost this round. You now have {Attemps} attemps\n')
        
        elif User_input == 'Paper' and Computer_choose == 'Rock':
            print(f'Congratulations!!!. You win the game with {Attemps} attemps')
            exit()
        
        elif User_input == 'Paper' and Computer_choose == 'Scissors':
            print(f'\nYou lost this round. You now have {Attemps} attemps\n')
        
        elif User_input == Computer_choose:
            print('\nDraw\n')
    print('\nGAME OVER')
    exit()

Welcome()
Main()
