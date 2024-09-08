from behavior import cadastro_curso, atualizar_curso, excluir_curso, mostrar_curso, cadastro_aluno, excluir_aluno, \
    mostrar_aluno, atualizar_aluno
from view import menu_principal, menu_curso, menu_aluno

while True:
    menu_principal()
    op = int(input("-> "))

    if op == 0:
        break
    elif op == 2:
        while True:
            menu_curso()
            choice = int(input("-> "))
            if choice == 0:
                break
            elif choice == 1:
                cadastro_curso()
            elif choice == 2:
                mostrar_curso()
            elif choice == 3:
                atualizar_curso()
            elif choice == 4:
                excluir_curso()
            else:
                print('Opcao invalida.')
            print('\n')
        print('\n')
    elif op == 1:
        while True:
            menu_aluno()
            choice = int(input("-> "))
            if choice == 0:
                break
            elif choice == 1:
                cadastro_aluno()
            elif choice == 2:
                mostrar_aluno()
            elif choice == 3:
                atualizar_aluno()
            elif choice == 4:
                excluir_aluno()
            else:
                print('Opcao invalida.')
            print("\n")
        print('\n')
    else:
        print("\n Inválido.")


