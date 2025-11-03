#!/usr/bin/env python3

import csv
from src.contas import *
from src.conta import *

if __name__ == "__main__":
    
    contas = Contas()

    arquivo = open('./src/contas.txt', 'r')
    leitor = csv.reader(arquivo)

    for linha in leitor:
        conta = ContaCorrente(linha[0], linha[1], float(linha[2]), float(linha[3]))
        contas.append(conta)

    arquivo.close()

    print('saldo - imposto')

    for c in contas:
        print('{} - {}'.format(c._saldo, c.get_valor_imposto()))