from model import School
from view import main_menu

if __name__ == '__main__':
    school = School()

    while True:
        main_menu()
        choice = int(input('Enter your choice: '))
        if choice == 0:
            break

        if choice == 1:
            print('\n--- Register ---')
            grades = []
            name = str(input("Student's name: "))
            for i in range(0, 3):
                grade = float(input(f' * '))
                grades.append(grade)

            name.upper()
            school.add_student(name, grades)
            print(f'{name} added.')

        elif choice == 2:
            print('\n--- Remove ---')
            name = str(input(" name: "))
            school.delete_students(name)

        elif choice == 3:
            print('\n--- Student List ----')
            school.show_students()

        elif choice == 4:
            print('\n--- Search Student ---')
            name = str(input('name = '))
            student_search(name)

        print("\n")