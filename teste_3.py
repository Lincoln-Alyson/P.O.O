from conta import Conta
from conta_especial import ContaEspecial
class verfica:
    if __name__ == '__main__':
        conta = Conta("31.345-X")
        conta.creditar(20)
        especial = ContaEspecial("31.567-X")
        conta.creditar(20)
        conta = especial
        conta.creditar(20)
        print(conta.get_saldo())

