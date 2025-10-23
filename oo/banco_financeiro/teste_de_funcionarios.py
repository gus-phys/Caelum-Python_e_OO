#!/usr/bin/env python3

from src.funcionarios import *

if __name__ == '__main__':
    diretor = Diretor('João', '111111111-11', 3000.0, '1234', 10)
    gerente = Gerente('José', '222222222-22', 5000.0, '1235', 5)
    cliente = Cliente('Maria', '333333333-33', '1236')

    sistema = SistemaInterno()
    sistema.login(diretor)
    sistema.login(gerente)
    sistema.login(cliente)