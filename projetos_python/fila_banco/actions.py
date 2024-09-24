from random import randint

from model import Bank, Client

bank = Bank()


def account_number_generator(list):
    serial = randint(1000000, 9999999)

    if serial in list:
        serial += 1
        return serial

    return serial


def account_verifier(serial):
    for a in bank.client_list:
        if serial == a.account_number:
            return True
    return False

def to_deposit(client,value):




# Menu Actions
def menu_options(op):
    if op == 1:
        print(f'\n--- Register ---')
        name = str(input('Name: '))
        document = str(input('Document: '))
        age = int(input('Age: '))

        serial = account_number_generator(bank.client_list)
        new_client = Client(serial, name, document, age)

        print(f'\n Done. Your account number {new_client.account_number}.')

        bank.client_list.append(new_client)

    elif op == 5:
        print('\n--- Show Clients ---')
        for a in bank.client_list:
            print(a)

    elif op == 2:
        print('\n--- Deposit ---')
        serial = int (input(' -Login: '))

        if account_verifier(serial):
            deposit = float(input("  $"))
