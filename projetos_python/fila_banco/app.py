from actions import menu_options
from view import main_menu

if __name__ == '__main__':

    while True:
        main_menu()
        op = int(input(" -> "))
        if op == 0:
            break
        menu_options(op)
        print('\n')



