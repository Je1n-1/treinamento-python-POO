items = []

class ItemCardapio:
    def __init__(self, tipo, tamanho, descricao, preco):
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao
        self.preco = preco
        self.preco_original = preco  # Armazena o preço original

class Sobremesa(ItemCardapio):
    def __init__(self, tipo, tamanho, descricao, preco):
        super().__init__(tipo, tamanho, descricao, preco)

    def __str__(self):
        return (
            f"Tipo: {self.tipo.ljust(25)} | "
            f"Tamanho: {self.tamanho.ljust(25)} | "
            f"Descrição: {self.descricao.ljust(25)}\n"
            f"Preço original: R${self.preco_original:<15.2f} | "
            f"Preço com desconto: R${self.preco:.2f}\n"
            f"{'----' * 30}"
        )

    def adicionar_item_cardapio_bebidas(self):
        if self not in items:
            items.append(self)
        else:
            print("Item já está no cardápio!")
    
    def adicionar_item_cardapio_pratos(self):
        if self not in items:
            items.append(self)
        else:
            print("Item já está no cardápio!")



    def aplicar_desconto_pratos(self):
            self.preco *= 0.92  # Aplica o desconto ao preço atual
    
    def aplicar_descontos_bebidas(self):
        self.preco *= 0.95

# Criando uma instância de Sobremesa
prato = Sobremesa('lasanha mexicana', 'médio', 'prato voltado para purista', 100.0)
bebida = Sobremesa('refrigerante', '2Litros', 'Guarana', 7)

#aplicando ao cardapio
prato.adicionar_item_cardapio_pratos()
bebida.adicionar_item_cardapio_bebidas()

# Aplicando desconto
prato.aplicar_desconto_pratos()
bebida.aplicar_descontos_bebidas()


for item in items:
    print(item)

