class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade}')


class ContaBanco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def mostrar_banco(self):
        print(f'Nome: {self.titular}\nSaldo: {self.saldo}')


class Animal:
    def __init__(self, especie):
        self.especie = especie

    def som(self):
        print("Emitindo som.")

    def mover(self):
        print("Movendo.")


class Cachorro(Animal):
    def __init__(self, nome):
        Animal.__init__(self,'Cachorro')
        self.nome = nome

    def som(self):
        print("AuAu")


class Gato(Animal):
    def __init__(self, nome):
        super().__init__('Gato')
        self.nome = nome

    def som(self):
        print("Miau.")


class Carro:
    def __init__(self, modelo, placa, ano):
        self._modelo = modelo
        self._placa = placa
        self._ano = ano

    def get_modelo(self):
        return self._modelo

    def get_placa(self):
        return self._placa

    def get_ano(self):
        return self._ano

    def set_modelo(self, modelo):
        self._modelo = modelo
        return self

    def set_placa(self, placa):
        self._placa = placa
        return self

    def set_ano(self, ano):
        self._ano = ano
        return self

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Empregado:
    def __init__(self, salario):
        self.salario = salario

    def adicionar_salario(self, valor):
        self.salario += valor


class Gerente(Pessoa, Empregado):
    def __init__(self, setor):
        Pessoa.__init__(self, 'Gerente')
        Empregado.__init__(self, 54890)
        self.setor = setor

    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade}')
        print(f'Setor: {self.setor}')
