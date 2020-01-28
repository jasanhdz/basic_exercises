# -*- coding: utf-8 -*-
from Book import ContactBook
import csv, os

def run():
    contact_book = ContactBook()

    if os.path.exists('contacts.csv'):
        with open('contacts.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for idx, row, in enumerate(reader):
                if idx == 0:
                    continue
                contact_book.add(row[0], row[1], row[2])
                
    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [A]dd contact 
            [U]pdate contact 
            [S]earch contact 
            [D]elete contact 
            [L]ist contacts 
            [E]xit
        ''')).lower()

        if command == 'a':
            name = str(input('write the name of the contact: '))
            phone = str(input('write the contact phone: '))
            email = str(input('write the contact email: '))
            
            contact_book.add(name, phone, email)

        elif command == 'u':
            name = str(input('write the name of the contact: '))
            contact_book.updateContact(name)
                
        elif command == 's':
            name = str(input('write the name of the contact: '))
            contact_book.search(name)

        elif command == 'd':
            name = str(input('write the name of the contact: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 'e':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()