def is_palindrome(string):
    return string == string[::-1]

while True:
    try:
        word = input('Enter a word: ')
        if word.isdigit():
            print('Please enter an alphabetic word and try again.\n')
        else:
            print(f'The word that you have chosen is {word}.\n')
        
        if is_palindrome(word):
            print(f'{word} IS a palindromic word.\n')
        else:
            print(f'{word} IS NOT a palindromic word.\n')
        
        print('\n')
        another_word = True if input('Do you want to try again? (Yes/No): ').lower() == 'yes' else False
        if another_word:
            print('Ok, lets try again.\n')
            print('\n')
        else:
            print('Ok, bye!!!')
            break
    except KeyboardInterrupt:
        print('Keyboard interrupt signal detected.')
        print('Exiting...')
        break
