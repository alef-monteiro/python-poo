import sqlite3


def connect_db():
    conn = sqlite3.connect('database.db')
    return conn


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        grade1 REAL,
        grade2 REAL,
        grade3 REAL
        )'''
    )

    conn.commit()
    conn.close()


def add_student_db(name, grades):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO students(name, grade1, grade2, grade3)
    VALUES (?,?,?,?)
    ''', (name, grades[0], grades[1], grades[2]))

    conn.commit()
    conn.close()  # grades
    # name is the key
    # grades is the key as list.


def update_student_db(name, grades):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE students
    SET grades = ?, name = ?
    WHERE name = ?    
    ''', (grades, name)
                   )


def remove_students_by_name(name):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM students
        WHERE name = ?
    ''', (name,))


def get_students_by_name(name):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM students
    WHERE name = ?
    ''', (name,))


def view_students():
    conn = sqlite3.connect('database.db')  # Conecte-se ao banco de dados
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students')  # Substitua 'students' pelo nome da tabela
    rows = cursor.fetchall()  # Obtenha todos os registros

    if not rows:
        print("A tabela está vazia.")
    else:
        print("Dados encontrados na tabela:")
        for row in rows:
            print(row)

    conn.close()
