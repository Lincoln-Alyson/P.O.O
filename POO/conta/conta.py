from contaAbstrata import ContaAbstrata
class Conta(ContaAbstrata):
    def __init__(self, numero):
        super().__init__(numero)

    def debitar(self, valor):
        self._saldo -= valor
