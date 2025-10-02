# Exercício 7: Múltiplas Classes Abstratas 
# Exemplo com transporte urbano

from abc import ABC, abstractmethod

class Rota(ABC):
    def __init__(self, distancia_km):
        self.distancia = distancia_km

    @abstractmethod
    def tempo_estimado(self):
        pass


class Tarifa(ABC):
    @abstractmethod
    def calcular_preco(self):
        pass


class UberX(Rota, Tarifa):
    def __init__(self, distancia_km):
        super().__init__(distancia_km)

    def tempo_estimado(self):
        # Supondo velocidade média de 40 km/h => 1,5 min por km
        tempo = self.distancia * 1.5
        print(f"Tempo estimado para {self.distancia} km: {tempo:.1f} minutos")

    def calcular_preco(self):
        # Preço base R$5 + R$3,20 por km
        preco = 5 + (self.distancia * 3.20)
        print(f"Preço total da corrida: R${preco:.2f}".replace(".", ","))


# Criando um objeto e testando
corrida = UberX(12)  # 12 km
corrida.tempo_estimado()
corrida.calcular_preco()
