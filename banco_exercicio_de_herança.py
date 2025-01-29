class Banco:
    def __init__(self, nome, endereco):
        self._nome = nome 
        self._endereco = endereco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self.numero = numero

    def __str__(self):
        return f'nome {self._nome.ljust(25)}| endereço {self._endereco.ljust(25)}| numero:{str(self.numero).ljust(25)}'

itau = Agencia('Itau', 'SP', 12345)
santander = Agencia('Santander', 'RJ', 123)

print('')
print(itau)
print(santander)