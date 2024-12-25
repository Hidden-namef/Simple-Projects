import random

Random_Number = random.randint(1, 100)
Attempts = 10

print('Welcome to the guessing number game\n')
while True:
    wanna_play = input('Do you want to play? (Yes/No): ').lower()
    print('\n')
    if wanna_play == 'yes':
        print('Ok, lets start!\n')
        break
    elif wanna_play == 'no':
        print('Oh ok... Bye!')
        exit()
    else:
        print('Please enter a valid answer: (Yes/No) and try again.\n')

print('I have generated a random number between 1 and 100.\n')
print('Your task is guess the number that i have generated.\n')
print('You have 10 attempts.\n')

while Attempts > 0:
    try:
        Attempt = int(input('Enter a number (1-100): '))
        print('\n')
    except ValueError:
        print('Please, enter a valid number (1-100) and try again.\n')
    
    if Attempt == Random_Number:
        print('Congratulations, you win!!!\n')
        print(f'You win with {Attempts} attempts.')
        exit()
    elif Attempt > Random_Number:
        Attempts -= 1
        print('The random number is LOWER than the number that you have entered.\n')
        print(f'Now you have {Attempts} attempts.\n')
    elif Attempt < Random_Number:
        Attempts -= 1
        print('The random number is HIGHER than the number that you have entered.\n')
        print(f'Now you have {Attempts} attempts.\n')
print('GAME OVER')
print(f'The number was {Random_Number}')
