from collections.abc import MutableSequence
from src.conta import Conta

class Contas(MutableSequence):
    
    _dados = []

    def __len__(self):
        return len(self._dados)
    
    def __getitem__(self, posicao):
        return self._dados[posicao]
    
    def __setitem__(self, posicao, valor):
        if (isinstance(valor, Conta)):
            self._dados[posicao] = valor
        else:
            raise TypeError("valor atribuído não é uma Conta")

    def __delitem__(self, posicao):
        del self._dados[posicao]

    def insert(self, posicao, valor):
        if (isinstance(valor, Conta)):
            return self._dados.insert(posicao, valor)
        else:
            raise TypeError("valor inserido não é uma Conta")   
