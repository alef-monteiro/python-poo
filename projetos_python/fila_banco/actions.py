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
client_data = Client


def menu_options(op):

    if op == 1:
        print(f'\n--- Register ---')
        name = str(input('Name: '))
        document = str(input('Document: '))
        age = int(input('Age: '))

        client_data._name = name
        client_data._document = document
        client_data._age = age
        bank.client_list.append(client_data)
        client_data._account_number = account_number_generator(client_data, bank.client_list)
        print(f'\n Done. Your account number {client_data.account_number}.')

    elif op == 2:
        print(f'\n--- Deposit ---\n')
        while True:
            account_number = int(input('Account number: '))
            if account_number_finder(account_number, client_data):
                value = float(input('\n -Deposit: '))
                to_deposit(client_data, value)
            else:
                tryagain = str(input('\n Invalid account.\n Try again (y/n): '))
                if tryagain.upper() == 'Y' or tryagain.upper() == 'y':
                    continue
                else:
                    break

    elif op == 3:
        print(f'\n--- Withdraw ---\n')
        while True:
            account_number = int(input('Account number: '))
            if account_number_finder(account_number, client_data):
                value = float(input('\n -Withdraw: '))
                to_withdraw(client_data, value)
            else:
                tryagain = str(input('\n Invalid account.\n Try again (y/n): '))
                if tryagain.upper() == 'Y' or tryagain.upper() == 'y':
                    continue
                else:
                    break

    elif op == 4:
        print(f'\n--- Balance ---\n')
        while True:
            account_number = int(input('Account number: '))

            if account_number_finder(account_number, client_data):
                client_data.__str__()
            else:
                tryagain = str(input('\n Invalid account.\n Try again (y/n): '))
                if tryagain.upper() == 'Y' or tryagain.upper() == 'y':
                    continue
                else:
                    break

    elif op == 5:
        bank.client_list.__str__()
