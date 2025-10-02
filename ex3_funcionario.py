# Ex3 - Exemplo de herança com construtores e super()

class Colaborador:
    def __init__(self, nome, pagamento):
        self.nome = nome
        self.pagamento = pagamento


class Supervisor(Colaborador):
    def __init__(self, nome, pagamento, setor):
        super().__init__(nome, pagamento)  
        self.setor = setor


if __name__ == "__main__":
    sup = Supervisor("Bruno", 9500, "Tecnologia")
    print(f"Supervisor: {sup.nome} | Salário: R$ {sup.pagamento:.2f} | Setor: {sup.setor}")
