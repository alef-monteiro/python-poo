import database
import report
from actions import to_register, to_remove, to_search, to_update, to_list
from model import School
from view import main_menu

if __name__ == '__main__':
    school = School()
    database.create_table()


    def exist_student(key):
        return key in school.students.keys()


    while True:
        main_menu()
        choice = int(input('Enter your choice: '))
        if choice == 0:
            break

        if choice == 1:
            to_register()

        elif choice == 2:
            to_remove()

        elif choice == 3:
            to_search()

        elif choice == 4:
            to_update()

        elif choice == 5:
            to_list()

        print("\n")

    database.view_students()
    report.generate_report()
