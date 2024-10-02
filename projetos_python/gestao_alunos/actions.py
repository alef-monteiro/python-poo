from model import School

school = School()


# School Actions -----------------
def exist_student(key):
    return key in school.students.keys()


def to_register():
    print('\n--- Register ---')
    grades = []
    name = str(input("Student's name: "))
    print('- grades')
    for i in range(0, 3):
        grade = float(input(f' * '))
        grades.append(grade)

    name = name.upper()
    school.add_student(name, grades)
    print(f'{name} added.')


def to_remove():
    print('\n--- Remove ---')
    name = str(input("name: "))
    name = name.upper()

    if exist_student(name):
        school.delete_students(name)
        print(f'{name} removed.')
    else:
        print(f'Student {name} not found.')


def to_list():
    print('\n--- Student List ----')
    school.show_students()


def to_search():
    print('\n--- Search Student ---')
    name = str(input('name = '))
    name = name.upper()
    if exist_student(name):
        print('Found it.')
        school.show_students()
    else:
        print('Not found.')


def to_update():
    print('\n--- Update Student ---')
    name = str(input('Name = '))
    name = name.upper()

    if exist_student(name):
        new_grades = []
        new_name = str(input(" New name: "))
        print('- New grades:')
        for i in range(0, 3):
            new_grade = float(input(f' * '))
            new_grades.append(new_grade)

        new_name = new_name.upper()
        school.updating_student(new_name, new_grades)
        print(f'{name} Updated.')
