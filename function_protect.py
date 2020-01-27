# -*- conding: utf-8 -*-

def protected(funct):
    def wrapper(password): 
        if password == 'platzi':
            return funct()
        else:
            print('La constraseña es incorrecta')

    return wrapper

@protected
def protected_func():
    print('Tu contraseña es correcta')


def decorator(funct):
    def wrapper(number):
        if number % 2 == 0:
            print('El número es par')
        else:
            return funct()
    return wrapper    

@decorator
def validation():
    print("El número no es par :(")
        

if __name__ == '__main__':
    # password = str(input('Ingresa tu contraseña: ')).lower()
    # protected_func(password)
    number = int(input('Ingresa un número entero: '))
    validation(number)