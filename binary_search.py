# -*- conding: utf-8 -*-
import random

def binary_search(numbers, number_to_find, low, high):
    if low > high:
        return False
    
    mid = int((low + high) / 2)
    
    if numbers[mid] == number_to_find:
        return True
    
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)


def sortList(numbers):
    numbers.sort()
    return numbers

def random_number_list(low, high, amount):
    numbers = random.sample(range(low, high), amount)
    return numbers

if __name__ == '__main__':
    # numbers = [51, 4, 67, 52, 16, 99, 100, 11, 25, 27, 18, 24, 46, 79, 31]
    numbers = random_number_list(1, 150, 100)
    ordered_list = sortList(numbers)
    # print(ordered_list)
    
    number_to_find = int(input('Enter a number: '))
    
    result = binary_search(ordered_list, number_to_find, 0, len(ordered_list) - 1)

    if result is True:
        print('If it is on the list. ')
    else:
        print('The number is unlisted')
    
    