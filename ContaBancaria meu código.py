class Conta_bancaria:
    def __init__(self, titular, saldo, ativo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo

    def __str__(self):
        return (f'titular{self.titular.ljust(25)} saldo:{str(self.saldo).ljust(25)}')
            
    def ativar_conta(self):
        if not self.ativo:
            self.ativo = True
            return True
        else:
            return False
    
alan = Conta_bancaria('Alan Rodrigues', 555.5, False)
jean = Conta_bancaria('Jean', 9999.9, True)

print(alan)
print(jean)