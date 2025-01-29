class ContaBancaria:
    '''
    Classe que representa uma conta bancária com titular, saldo e status (ativo ou não).
    '''

    def __init__(self, titular, saldo):
        # Usando propriedades para garantir que os valores sejam válidos ao serem definidos
        self._titular = titular
        self._saldo = saldo
        self._ativo = False  # A conta começa inativa por padrão

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, status):
        # Garantir que o status seja um valor booleano
        if isinstance(status, bool):
            self._ativo = status
        else:
            raise ValueError("O status deve ser um valor booleano.")

    def __str__(self):
        # Método especial __str__ para representar a instância de maneira formatada
        return f'Titular: {self._titular} | Saldo: R${self._saldo:.2f} | Ativo: {"Sim" if self._ativo else "Não"}'

    @classmethod
    def ativar_conta(cls, conta):
        # Método de classe que ativa a conta bancária
        conta.ativo = True
        return f'A conta de {conta.titular} foi ativada.'

# Criando instâncias da classe ContaBancaria
conta1 = ContaBancaria('Ana Silva', 1500.00)
conta2 = ContaBancaria('Carlos Santos', 2500.00)

# Imprimindo as instâncias
print(conta1)
print(conta2)

# Usando o método de classe para ativar a conta
ContaBancaria.ativar_conta(conta1)

# Imprimindo o status de ativo após ativar a conta
print(f'Conta1 - Ativo: {conta1.ativo}')

# Usando a propriedade titular
print(f'Titular da Conta1: {conta1.titular}')
