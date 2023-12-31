from abc import ABC, abstractmethod

class ContaAbstrata(ABC):
    def __init__(self, numero):
        self._numero = numero
        self._saldo = 0

    def creditar(self, valor):
        self._saldo = self._saldo + valor

    @property
    @abstractmethod
    def debitar(self, valor):
        pass

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self._numero = numero
