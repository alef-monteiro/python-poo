from random import randint

from model import Bank, Client


# Client Actions
def to_deposit(client, value):
    client.account_balance(value)
    return client.__str__()


def to_withdraw(client, value):
    value = (-1) * value
    client.account_balance(value)
    return client.__str__()


def account_number_generator(client, client_list):
    while True:
        new_account = randint(10000000, 9999999999)
        return new_account
        # if all(new_account != client.account_number for client in client_list):
        #     client._account_number = new_account
        #     return new_account


def account_number_finder(number, client_list):
    for _, client in enumerate(client_list):
        if client.account_number == number:
            return True

    return False


# Menu Actions
bank = Bank()


def menu_options(op):
    if op == 1:
        print(f'\n--- Register ---')
        name = str(input('Name: '))
        document = str(input('Document: '))
        age = int(input('Age: '))

        new_client = Client(name, document, age)
        new_client._account_number = account_number_generator(new_client, bank)
        print(f'\n Done. Your account number {new_client.account_number}.')

        bank.client_list.append(new_client)
    if op == 5:
        print('\n--- Show Clients ---')


