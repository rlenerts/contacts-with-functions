# IZVEIDOSIM KONTAKTU APLIKĀCIJU IZMANTOJOT:
# Funkcijas
# Datu struktūras (JSON)
# File I/O
import json

contacts = []

def LoadContacts():
   with open('contacts.json', 'r', encoding='UFT8') as file:
        json.load(contacts, file, indent = 4)
        

def PrintContacts():
  for contact in contacts:
    print(f"{contact['name']} {contact['surname']} {contact['number']} {contact['email']}")


def Addcontact():
        name = input('Enter name: ')
        surname = input('Enter surname: ')
        number = input('Enter number: ')
        email = input('Enter email: ')

        contact = {
            'name': name, 
            'surname': surname, 
            'number': number,
            'email': email
        }
        contacts.append(contact)

def SaveContacts():
  with open('contacts.json' , 'w' , encoding='UTF8') as file:
    json.dump(contacts, file, indent =4 )



while(True):

    response = input('N-add new, P-print, E-exit: ')
    if response == 'N':
        Addcontact()
        SaveContacts()
    elif response == 'P':
      PrintContacts()
      LoadContacts()
    elif response == 'E':
        break


