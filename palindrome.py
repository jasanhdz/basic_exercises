# -*- conding: utf-8 -*-
def palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)
    
    reversed_word = ''.join(reversed_letters)
    
    if reversed_word == word:
        return True
    else:
        return False

def palindrome2(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True

    return False

def run():
    word = str(input("Write a word: "))
    result = palindrome2(word)
    
    if result is True:
        print('{} is a palindrome...'.format(word))
    else:
        print('{} is a not a palindrome'.format(word))
    

if __name__ == '__main__':
    run()