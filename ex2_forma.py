# Ex2 - Exemplo de classe abstrata e implementação concreta

from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        """Método abstrato que deve ser implementado nas subclasses"""
        pass


class Quadrilatero(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


if __name__ == "__main__":
    q1 = Quadrilatero(7, 3)
    q2 = Quadrilatero(4.5, 2)

    print(f"Área do primeiro quadrilátero: {q1.area()} unidades²")
    print(f"Área do segundo quadrilátero: {q2.area()} unidades²")
