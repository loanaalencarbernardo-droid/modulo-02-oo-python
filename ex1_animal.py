# Ex1 - Herança simples com classes em Python

class SerVivo:
    def __init__(self, apelido):
        self.apelido = apelido

    def emitir_som(self):
        print("Som genérico do ser vivo")


class Cao(SerVivo):
    def __init__(self, apelido):
        
        super().__init__(apelido)

    def emitir_som(self):
        print("Au au! Latido de cachorro")


if __name__ == "__main__":
    bicho = SerVivo("Criatura")
    pet = Cao("Bolt")

    print(f"Nome do ser vivo: {bicho.apelido}")
    bicho.emitir_som()

    print(f"Nome do cão: {pet.apelido}")
    pet.emitir_som()
