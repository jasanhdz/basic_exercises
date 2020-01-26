# -*- coding: utf8 -*-
import random

def run():
    number_found = False
    print(" Welcome I invite you to play: guess the number ")
    initial_number = int(input("Enter the minimum number: "))
    range_number = int(input('Enter the maximum number:  '))
    random_number = random.randint(initial_number, range_number)
    
    while not number_found:
        number = int(input("Try a number: "))

        if number == random_number:
            print('Congratulations. you found the number')
            number_found = True
        elif number > random_number:
            print('The number is smaller')
        else:
            print('The number is a bigger')

if __name__== '__main__':
    run()

