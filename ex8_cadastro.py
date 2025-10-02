# Exercício 8: Abstração e Herança para Sistema de Cadastro
# Sistema de cadastro de usuários e parceiros

from abc import ABC, abstractmethod

class Registro(ABC):
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    @abstractmethod
    def exibir_dados(self):
        pass


class Usuario(Registro):
    def __init__(self, codigo, nome, data_entrada):
        super().__init__(codigo, nome)
        self.data_entrada = data_entrada

    def exibir_dados(self):
        print(f"Usuário:\n - Nome: {self.nome}\n - Código: {self.codigo}\n - Data de entrada: {self.data_entrada}\n")


class Parceiro(Registro):
    def __init__(self, codigo, nome, inscricao_estadual):
        super().__init__(codigo, nome)
        self.inscricao_estadual = inscricao_estadual

    def exibir_dados(self):
        print(f"Parceiro:\n - Nome: {self.nome}\n - Código: {self.codigo}\n - Inscrição Estadual: {self.inscricao_estadual}\n")


def listar_registros(lista_registros):
    for registro in lista_registros:
        registro.exibir_dados()


# Criando lista de objetos mistos
cadastros = [
    Usuario(101, "Carlos Silva", "10/03/2022"),
    Parceiro(202, "Loja Central", "123.456.789.000"),
    Usuario(103, "Fernanda Alves", "25/11/2023"),
    Parceiro(204, "Mercado Bom Preço", "987.654.321.000")
]

listar_registros(cadastros)
