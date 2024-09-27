class School:
    def __init__(self):
        self.students = {}

    # CREATE
    def add_student(self, name, grade):
        self.students[name] = grade

    # DELETE
    def delete_students(self, key):
        del self.students[key]

    # UPDATE
    def updating_student(self, name, new_grade):
        if name in self.students:
            self.students[name] = new_grade
            return True
        else:
            return False

    # READ
    def show_students(self):