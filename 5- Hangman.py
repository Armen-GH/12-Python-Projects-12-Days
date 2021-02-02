import random
import string
from words import data 

def valid_word(data):
    word = random.choice(data)
    while '-' in data or ' ' in data:
        word = random.choice(data)
    return word.upper()

def hangman():
    word = valid_word(data)
    
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word)
    used_letters = set()

    lives = 6 
    
    while len(word_letters) > 0 and lives > 0:
        print('you have ', lives, 'remaining and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                print('Wrong letter!')
                lives = lives - 1
        else:
            print(f'{user_letter}Seems like an invalid input')
        
        
    
    if lives == 0:
        print('Sorry you lost, the word was ', word)
    else:
        print('you correctly guessed the word ', word,'!!')

hangman()
