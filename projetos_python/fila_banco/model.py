class Bank:
    def __init__(self):
        self.client_list = []
        # queue is first in, first out

    def __str__(self):
        return str(self.client_list)

    def enqueue_clients(self, clients):
        self.client_list.append(clients)
        return f'Enqueued {len(clients)} clients'

    def dequeue_clients(self):
        if not self.client_list.is_empty():
            self.client_list.pop(0)
            return f'Dequeued {len(self.client_list)} clients'

        return f'Empty.'

    def show_clients(self):
        return self.client_list

    def queue_empty(self):
        return self.client_list.is_empty()


class Client:

    def __init__(self, account_number, name, document, age):
        self._account_number = account_number
        self._name = name
        self._age = age
        self._document = document
        self._account_balance = 0

    def __str__(self):
        return (f'Account Number: {self._account_number}'
                f'\nName: {self._name}'
                f'\nBalance: {self._account_balance}')

    # Getter para _account_balance
    @property
    def account_balance(self):
        return self._account_balance

    # Setter para _account_balance
    @account_balance.setter
    def account_balance(self, value):
        self._account_balance += value

    # Getter para _id
    @property
    def id(self):
        return self._id

    # Setter para _id
    @id.setter
    def id(self, value):
        self._id = value

    # Getter para _account_number
    @property
    def account_number(self):
        print(self._account_number)
        return self._account_number

    # Setter para _account_number
    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    # Getter para name
    @property
    def name(self):
        return self._name

    # Setter para name
    @name.setter
    def name(self, value):
        self._name = value

    # Getter para _document
    @property
    def document(self):
        return self._document

    # Setter para _document
    @document.setter
    def document(self, value):
        self._document = value
