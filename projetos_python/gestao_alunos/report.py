import csv

import database


def generate_report():
    conn = database.connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()

    # Criando o arquivo vazio
    file = 'student.csv'

    # Abrir o arquivo CSV para escrever
    with open(file, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['id', 'name', 'grade 1', 'grade 2', 'grade 3'])
        for student in students:
            writer.writerow([student[0], student[1], student[2], student[3]])
