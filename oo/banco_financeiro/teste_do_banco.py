#!/usr/bin/env python3

from src.conta import *
from src.manipulador import *

if __name__ == '__main__':
    # banco = conta.Banco('Banco Caelum')
    
    # # c = conta.Conta('123-4', 'Joao', 1000.0)
    # cc = conta.ContaCorrente('123-5', 'José', 1000.0)
    # cp = conta.ContaPoupanca('123-6', 'Maria', 1000.0)
    # ci = conta.ContaInvestimento('123-7', 'Ana', 1000.0)

    # # banco.adiciona(c)
    # banco.adiciona(cc)
    # banco.adiciona(cp)
    # banco.adiciona(ci)

    # print("\n" + "="*40)
    # print("--- Testando 'AtualizadorDeContas' ---")
    # for i in range(banco.pagaTotalDeContas()):
    #     conta_cliente = banco.pagaConta(i)
    #     print("\n>>> {} <<< \nTitular: {}".format(
    #         conta_cliente.__class__.__name__, 
    #         conta_cliente._titular
    #         ))
    #     adc = conta.AtualizadorDeContas(.01)
    #     adc.roda(conta_cliente)

    # print("\n--- Testando o método 'roda' ---")
    # cliente =  conta.Cliente('Luis', 'Otávio', '123.456.789-10')
    # adc = conta.AtualizadorDeContas(.01)
    # adc.roda(cliente)
    
    # print("\n--- Extrato de uma conta ---")
    # print(ci)

    cc1 = ContaCorrente('123-4', 'João', 1000)
    cc2 = ContaCorrente('123-5', 'José', 1000)
    seguro1 = SeguroDeVida(100, 'José', '345-77')
    seguro2 = SeguroDeVida(200, 'Maria', '237-98')

    lista_tributraveis = []
    lista_tributraveis.append(cc1)
    lista_tributraveis.append(cc2)
    lista_tributraveis.append(seguro1)
    lista_tributraveis.append(seguro2)

    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributraveis)

    print(total)