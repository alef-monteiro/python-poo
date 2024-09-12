import sqlite3

import requests

from db.database import ConnectionSQLite
from model import Contact


class AgendaActions:
    @staticmethod
    def get_zip_code(zip_code: str):
        api_url = f'https://viacep.com.br/ws/{zip_code}/json/'
        response = requests.get(api_url)
        data = response.json()
        if 'erro' in data:
            return None

        return data

@staticmethod
def save_contact(contact: Contact):
    _connection_sqlite = ConnectionSQLite()
    _conn = _connection_sqlite.connect()

    if not _conn:
        return _conn

    try:
        cursor = _conn.cursor()
        _script = '''
        INSERT INTO contacts (name, email, cell_phone, zip_code, street, neighborhood, city, state)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        _values = (
            contact.name,
            contact.email,
            contact.cell_phone,
            contact.zip_code,
            contact.street,
            contact.neighborhood,
            contact.city,
            contact.state,
        )
        cursor.execute(_script, _values)
        _conn.commit()

        print("Contact savedn successfully")
        return 'Contact saved successfully.'
    except sqlite3.Error as error:
        print(f'Error inserting contact: {error}')
        return 'Error inserting contact'
