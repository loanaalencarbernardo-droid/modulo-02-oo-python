# Exercício 6: Classe Abstrata com Método Concreto
# Criando hierarquia de contas bancárias

from abc import ABC, abstractmethod

class BancoConta(ABC):
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    @abstractmethod
    def sacar(self, valor):
        pass

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


class ContaSimples(BancoConta):
    def __init__(self, saldo_inicial, titular, numero_conta):
        super().__init__(saldo_inicial)
        self.titular = titular
        self.numero_conta = numero_conta

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado na conta de {self.titular} ({self.numero_conta}).")
        else:
            print(f"Saque de R${valor:.2f} não autorizado! Saldo insuficiente na conta de {self.titular}.")


# Criando várias contas
lista_contas = [
    ContaSimples(1200, "Carlos", "001-2"),
    ContaSimples(600, "Fernanda", "003-4"),
    ContaSimples(2500, "Rafael", "005-6")
]

# Testando os métodos
for conta in lista_contas:
    print("-----")
    conta.sacar(200)
    conta.verificar_saldo()

print("-----")
