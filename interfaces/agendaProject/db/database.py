import sqlite3

DATABASE_NAME = 'db/agenda.db'


class ConnectionSQLite:
    def __init__(self):
        self.db_name = DATABASE_NAME
        self.conn = None

    def connect(self):
        # Creates the connection to the db.
        try:
            self.conn = sqlite3.connect(self.db_name)
            print(f"Connected to database {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return f"Error connecting to database: {e}"
        return self.conn

    def disconnect(self):
        # Closes the connection to the db.
        if self.conn:
            self.conn.close()
            print(f"Connection with {self.db_name} has been closed.")


class CreateDataBaseSQLite:

    def __init__(self):
        self._connection_sqlite = ConnectionSQLite()

    @staticmethod
    def _create_table(connection):
        # Creates a table in the db.
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                cell_phone TEXT,
                zip_code TEXT,
                street TEXT,
                neighborhood TEXT,
                city TEXT,
                state TEXT
                );
            """)
            connection.commit()
            print("Table created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def run_script(self):
        _conn = self._connection_sqlite.connect()

        if _conn:
            self._create_table(connection=_conn)
            self._connection_sqlite.disconnect()