from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass

    def __str__(self):  # Representação em formato bonito
        return f"{self.marca} {self.modelo}\n_____________________________________"

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def ligar(self):
        return f"O carro {self.marca} {self.modelo} está ligado!"
     
    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}, Cor: {self.cor}\n_____________________________________________________________"
