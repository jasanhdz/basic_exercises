# -*- coding: utf-8 -*-

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cypher(message):
    words = message.split(' ')
    crypher_message = []
    
    for word in words:
        crypher_word = ''
        for letter in word:
            crypher_word += KEYS[letter]
        
        crypher_message.append(crypher_word)

    return ' '.join(crypher_message)

def decipher(message):
    words = message.split(' ')
    decipher_message = []
    
    for word in words:
        decipher_word = ''
        
        for letter in word:
            
            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key
        
        decipher_message.append(decipher_word)
    
    return ' '.join(decipher_message)

def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---
Welcome to cryptography. What do you want to do?

    [e]ncrypt message
    [d]ecrypt message
    [g]o out
        '''))

        if command == 'e':
            message = str(input('Write your message: '))
            crypher_message = cypher(message)
            print(crypher_message)
        elif command == 'd':
            message = str(input('Write your encrypt message: '))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 'g':
            print('go out')
            break
        else:
            print('¡Invalid command!')


if __name__ == '__main__':
    print('E N C R Y P T E D  M E S S A G E S')
    run()