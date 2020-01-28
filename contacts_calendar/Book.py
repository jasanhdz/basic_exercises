# -*- encoding: utf-8 -*-
import csv

from Contact import Contact
class ContactBook:
    def __init__(self):
        self._contacts = []
    
    def save(self):
        with open('contacts.csv', 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email') )
            
            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )
    
    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self.save()
        
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
        else:
            print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
            print("No hay contactos en el directorio :(")
            print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
            
    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self.save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()
    
    def updateContact(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                while True:      
                    value = str(input('''
    ¿What value do you want to change?
            
        [N]ame
        [P]hone
        [E]mail
        [G]o out or none    
                            
                    ''')).lower()
                    if value == 'n':
                        name = str(input('Enter the new name: '))
                        contact.name = name
                        self.save()
                        print('name updated successfully...')
                    elif value == 'p':
                        phone = str(input('Enter the new phone: '))
                        contact.phone = phone
                        self.save()
                        print('Phone updated successfully...')
                    elif value == 'e':
                        email = str(input('Enter the new email: '))
                        contact.email = email
                        self.save()
                        print('Email updated successfully...')
                    else:
                        print('Leaving the contact update')
                        break
        else:
            self._not_found()
    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * ---')
        print('Name: {}'.format(contact.name))
        print('Phone: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * ---')
    
    def _not_found(self):
        print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
        print('User not found! :O')
        print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')