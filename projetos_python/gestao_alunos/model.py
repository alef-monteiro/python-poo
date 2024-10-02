class School:
    def __init__(self):
        self.students = {}

    # CREATE
    def add_student(self, name, grade):
        self.students[name] = grade

    # DELETE
    def delete_students(self, key):
        # Apenas perguntar se a chave está dentro do dicionário basta
        del self.students[key]

    # UPDATE
    def updating_student(self, name, new_grade):
        if name in self.students:
            self.students[name] = new_grade
            print(f'Updated student {name}')
        else:
            print(f'Student {name} not found')

    # READ
    def show_students(self):
        # Sempre verificar se a lista está vazia
        if not self.students:
            print("There are no students")
        else:
            for student, grades in self.students.items():
                print(f" Name: {student} - {grades}")
