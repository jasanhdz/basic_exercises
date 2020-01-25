# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_square(dave)

def make_square(turtle):
    length = int(input('Tamaño de cuadrado: '))
    # iterator 4 times
    for i in range(4):
        make_line_and_turn(turtle, length)
  
def make_line_and_turn(turtle, length):
    turtle.forward(length)
    turtle.left(90)

if __name__ == '__main__':
    main()
        