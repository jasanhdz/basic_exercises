# -*- conding: utf-8 -*-
import random

IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
        |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''','''
   ''']     

WORDS = [
    'couch',
    'dryer',
    'government',
    'deputy',
    'democracy',
    'computer',
    'keyboard',
    'washing machine',
]

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * ---')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    
    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Chose a letter: '))
        
        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        
        if len(letter_indexes) == 0:
            tries += 1
            
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('The correct word was: {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            
            letter_indexes = []
        
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('¡Congratulations! Won. The word is {}'.format(word))
            break

if __name__ == '__main__':
    print('W E L C O M E  T O  H A N G E D')
    run()