from model import Curso, Aluno

lista_cursos = []
lista_alunos = []


def cadastro_curso():
    nome_curso = input('\nNome: ')
    turno_curso = input('Turno: ')
    dados_curso = Curso(nome_curso, turno_curso)
    lista_cursos.append(dados_curso)

    print("Cadastrado!")


def mostrar_curso():
    print("\n-- Cursos --")
    for i, a in enumerate(lista_cursos):
        print(f'{i} {a.__ref__()}')


def atualizar_curso():
    print()
    mostrar_curso()
    print("--- Escolha ---")
    valor = int(input("-> "))

    for i, _ in enumerate(lista_cursos):
        if valor == i:
            lista_cursos[i].nome_curso = input('Nome: ')
            lista_cursos[i].turno = input('Turno: ')

            print("Atualizado!")
        elif valor > len(lista_cursos) or valor < 0:
            print("\nValor Inválido*.")


def excluir_curso():
    print()
    mostrar_curso()
    print("--- Escolha ---")
    valor = int(input("-> "))

    for i, a in enumerate(lista_cursos):
        if valor == i:
            del lista_cursos[i]
            print("Excluído!")
        elif valor > len(lista_cursos) or valor < 0:
            print("\n**Valor Inválido.")


# ----------- Aluno


def cadastro_aluno():
    nome_aluno = input('Nome: ')
    idade_aluno = input('Idade: ')
    curso_nome = str
    turno = str

    mostrar_curso()
    print("--- Escolha ---")
    valor = int(input('-> '))

    for i, _ in enumerate(lista_cursos):
        if valor == i:
            curso_nome = lista_cursos[i].nome_curso
            turno = lista_cursos[i].turno

        elif valor > len(lista_cursos) or valor < 0:
            print("\nCurso inválido.")
            return cadastro_aluno()

    aluno_dados = Aluno(nome_aluno, idade_aluno, curso_nome, turno)
    lista_alunos.append(aluno_dados)
    return

def mostrar_aluno():
    for i, a in enumerate(lista_alunos):
        print(f'{i} {a.__ref__()}')
        print(' ------ ')


def atualizar_aluno_curso():
    mostrar_curso()
    print("--- Escolha ---")
    valor = int(input('-> '))

    novo_curso = str
    novo_turno = str

    for i, _ in enumerate(lista_cursos):
        if valor == i:
            novo_curso = lista_cursos[i].get_nome_curso()
            novo_turno = lista_cursos[i].get_turno_curso()

            return novo_curso, novo_turno

        elif valor > len(lista_cursos) or valor < 0:
            return atualizar_aluno_curso()


def atualizar_aluno():
    print()
    mostrar_aluno()
    print("--- Escolha ---")
    valor = int(input('-> '))

    for i, _ in enumerate(lista_alunos):
        if valor == i:
            lista_alunos[i].nome = input('Nome: ')
            lista_alunos[i].idade = input('Idade: ')

            print(" > Deseja mudar curso (1/0)\n")
            a = int(input(' -> '))

            if a == 0:
                print("Atualizado!")
            elif a == 1:
                lista_alunos[i].curso, lista_alunos[i].turno = atualizar_aluno_curso()
            elif valor > len(lista_alunos) or valor < 0:
                print("Erro.")


        elif valor > len(lista_alunos) or valor < 0:
            print("Erro.")
            return atualizar_aluno()


def excluir_aluno():
    mostrar_aluno()
    print("--- Escolha ---")
    valor = int(input('-> '))

    for i, _ in enumerate(lista_alunos):
        if valor == i:
            del lista_alunos[i]

        elif valor > len(lista_alunos) or valor < 0:
            print("\n Erro.")
            return excluir_aluno()
