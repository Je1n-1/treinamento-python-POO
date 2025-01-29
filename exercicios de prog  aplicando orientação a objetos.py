class Carro:
    def __init__(self, modelo, cor, ano):
        self._modelo = modelo
        self._cor = cor
        self._ano = ano

    def caracteristicas_carro(self):
        return (
            f"Modelo: {self._modelo.ljust(30)} "
            f"Cor: {self._cor.ljust(20)} "
            f"Ano: {str(self._ano).ljust(10)}"
        )

vectra = Carro("Vectra GT", "Prata", 2011)
astra = Carro("Astra Gsi", "Branco", 2005)
kadett = Carro("Kadett", "Vermelho", 1990)

print("=== Características dos Carros ===")
print(vectra.caracteristicas_carro())
print(astra.caracteristicas_carro())
print(kadett.caracteristicas_carro())
print("")


class Restaurante:
    def __init__(self, nome, categoria, ativo, tipo, cidade):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.tipo = tipo
        self.cidade = cidade

    def __str__(self):
        status = "Ativo" if self.ativo else "Inativo"
        return (
            f"Restaurante: {self.nome.ljust(25)} "
            f"Categoria: {self.categoria.ljust(15)} "
            f"Status: {status.ljust(10)} "
            f"Tipo: {self.tipo.ljust(15)} "
            f"Cidade: {self.cidade.ljust(20)}"
        )

restaurante_lasanha = Restaurante("Restaurante Lasanha", "Familiar", True, "Curtição", "Ponta Grossa")
restaurante_hamburguer = Restaurante("Restaurante Hamburguer", "Fast-food", False, "Perdição", "Panambi")

print("=== Detalhes dos Restaurantes ===")
print(restaurante_hamburguer)
print(restaurante_lasanha)
print("")


class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return (
            f"Cliente: {self.nome.ljust(25)} "
            f"Idade: {str(self.idade).ljust(10)} "
            f"Email: {self.email.ljust(30)} "
            f"Telefone: {self.telefone.ljust(15)}"
        )

cliente1 = Cliente("Ana Silva", 28, "ana.silva@example.com", "99999-1234")
cliente2 = Cliente("Carlos Santos", 35, "carlos.santos@example.com", "98888-5678")
cliente3 = Cliente("Mariana Oliveira", 22, "mariana.oliveira@example.com", "97777-9101")

print("=== Detalhes dos Clientes ===")
print(cliente1)
print(cliente2)
print(cliente3)
