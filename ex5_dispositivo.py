# Exercício 5: Herança em Múltiplos Níveis (Hierarquia)
# Criar 3 níveis de herança entre classes

class AparelhoEletronico:
    def __init__(self):
        pass

    def ligar(self):
        print("O aparelho está ligado.")

    def desligar(self):
        print("O aparelho foi desligado.")


class Computador(AparelhoEletronico):
    def __init__(self):
        super().__init__()

    def instalar_programa(self, nome_programa):
        print(f"O programa {nome_programa} foi instalado com sucesso.")


class Laptop(Computador):
    def __init__(self):
        super().__init__()

    def verificar_bateria(self, nivel):
        print(f"Nível atual da bateria: {nivel}%.")



meu_laptop = Laptop()


meu_laptop.ligar()
meu_laptop.desligar()


meu_laptop.instalar_programa("Python 3.12")


meu_laptop.verificar_bateria(85)
