from random import randint

from model import Bank, Client

bank = Bank()


def account_number_generator(list):
    serial = randint(1000000, 9999999)

    if serial in list:
        serial += 1
        return serial
    return serial


def account_verifier(login):
    for a in bank.client_list:
        if login == a.account_number:
            return a, True
    return None, False


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

    elif op == 4:
        print('\n--- Show Clients ---')
        for a in bank.client_list:
            print(a)
            print("-----------")

    elif op == 2:
        print('\n--- Deposit ---')
        login = int(input(' -Login: '))
        client, verify = account_verifier(login)
        if verify:
            deposit = float(input(' -Deposit: $'))
            client.account_balance = deposit
            print(f' Done. Your balance: ${client.account_balance}')
        else:
            print(' Something went wrong. Please try again.')

    elif op == 3:
        print('\n--- Withdraw ---')
        login = int(input(' -Login: '))
        client, verify = account_verifier(login)
        if verify:
            withdraw = float(input(' -Withdraw: $'))
            client.account_balance = withdraw*(-1)
            print(f' Done. Your balance: ${client.account_balance}')
        else:
            print(' Something went wrong. Please try again.')

