from model import School
from view import main_menu

if __name__ == '__main__':
    while True:
        main_menu()
        choice = input('Enter your choice: ')
        if choice == '0':
            break
        elif choice == '1':
            
