# Ex4 - Abstração com propriedades e herança

from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def acelerar(self, incremento):
        """Método que deve ser implementado para aumentar a velocidade"""
        pass

    @property
    @abstractmethod
    def rodas(self):
        """Propriedade obrigatória nas subclasses"""
        pass


class Automovel(Transporte):
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0
        self._rodas = 4

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"{self.modelo} ganhou velocidade: {self.velocidade} km/h")

    @property
    def rodas(self):
        return self._rodas


class Motocicleta(Transporte):
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0
        self._rodas = 2

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"{self.modelo} acelerou forte: {self.velocidade} km/h")

    @property
    def rodas(self):
        return self._rodas


if __name__ == "__main__":
    carro1 = Automovel("Corolla")
    carro1.acelerar(20)
    carro1.acelerar(15)
    print(f"O {carro1.modelo} possui {carro1.rodas} rodas.\n")

    moto1 = Motocicleta("Yamaha MT-03")
    moto1.acelerar(25)
    moto1.acelerar(30)
    print(f"A {moto1.modelo} possui {moto1.rodas} rodas.")
