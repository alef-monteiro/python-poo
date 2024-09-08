import random


class Curso:
    def __init__(self, nome_curso, turno):
        self.nome_curso = nome_curso
        self.turno = turno

    def __ref__(self):
        return f'{self.nome_curso} - {self.turno}'

    def get_nome_curso(self):
        return self.nome_curso

    def get_turno(self):
        return self.turno

    # -------------

    def set_nome_curso(self, nome_curso):
        self.nome_curso = nome_curso

    def setturno(self, turno):
        self.turno = turno


def gerar_matricula():
    return random.randint(100, 999)


class Aluno(Curso):
    def __init__(self, nome, idade, curso, turno):
        self._nome = nome
        self._idade = idade
        self._matricula = gerar_matricula()
        self._curso = Curso(curso, turno)

    def __ref__(self):
        return f' - Nome:{self._nome} - Idade:{self._idade}\nMatricula: {self._matricula} - Turma:{self._curso.get_nome_curso()}'

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def get_matricula(self):
        return self._matricula

    def get_curso(self):
        return self._curso

    # -------------

    def set_idade(self, idade):
        self._idade = idade

    def set_matricula(self, matricula):
        self._matricula = matricula

    def set_curso(self, curso):
        self._curso = curso
