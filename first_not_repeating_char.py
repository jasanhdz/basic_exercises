# -*- coding: utf-8 -*-

def first_not_repeating_char(string):
    seen_letters  = {}
  
    for idx, letter in enumerate(string):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append( (key, value[0]) )
    
    order_final_letters = sorted(final_letters, key=lambda value: value[1])
    if order_final_letters:
        return order_final_letters[0][0]
    else: 
        return '_'
    
if __name__ == '__main__':
    char_sequence = str(input('Write a sequence of characters: '))
    result = first_not_repeating_char(char_sequence)
    
    if result == '_':
        print('All characters are repeated')
    else:
        print('The first non-repeated character is: {} '.format(result))
    