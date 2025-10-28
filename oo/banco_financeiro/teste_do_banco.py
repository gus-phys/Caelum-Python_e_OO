#!/usr/bin/env python3

from src.conta import *
from src.manipulador_tributaveis import ManipuladorDeTributaveis
from src.tributavel import Tributavel

if __name__ == '__main__':
    banco = Banco('Banco Caelum')
    
    # c = Conta('123-4', 'Joao', 1000.0)
    cc = ContaCorrente('123-5', 'José', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)
    ci = ContaInvestimento('123-7', 'Ana', 1000.0)

    # banco.adiciona(c)
    banco.adiciona(cc)
    banco.adiciona(cp)
    banco.adiciona(ci)

    print("\n" + "="*40)
    print("--- Testando 'AtualizadorDeContas' ---")
    for i in range(banco.pagaTotalDeContas()):
        conta_cliente = banco.pagaConta(i)
        print("\n>>> {} <<< \nTitular: {}".format(
            conta_cliente.__class__.__name__, 
            conta_cliente._titular
            ))
        adc = AtualizadorDeContas(.01)
        adc.roda(conta_cliente)

    print("\n--- Testando o método 'roda' ---")
    cliente =  Cliente('Luis', 'Otávio', '123.456.789-10')
    adc = AtualizadorDeContas(.01)
    adc.roda(cliente)
    
    print("\n--- Extrato de uma conta ---")
    print(ci)

    print("\n" + "="*40)
    print("--- Testando 'ManipuladorDeTributaveis' ---")
    cc1 = ContaCorrente('123-4', 'João', 1000)
    cc2 = ContaCorrente('123-5', 'José', 1000)
    seguro1 = SeguroDeVida(100, 'José', '345-77')
    seguro2 = SeguroDeVida(200, 'Maria', '237-98')

    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida)
    # Tributavel.register(ContaPoupanca)  # Apenas para teste, ContaPoupanca não é tributável
    Tributavel.register(ContaInvestimento)

    lista_tributaveis = []
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)
    lista_tributaveis.append(cp)  # ContaPoupanca não é tributável
    lista_tributaveis.append(ci)

    for conta_cliente in lista_tributaveis:
        if (isinstance(conta_cliente, Tributavel)):
            print("{} de {}: R$ {}".format(
                conta_cliente.tipo,
                conta_cliente._titular,
                conta_cliente.get_valor_imposto()
                ))
        else:
            print("{} de {}: não tributável".format(
                conta_cliente.tipo,
                conta_cliente._titular
                ))

    mt = ManipuladorDeTributaveis()
    print("\nCalculando impostos...")
    total = mt.calcula_impostos(lista_tributaveis)
    print("\nTotal: R$ {}".format(total))

    # print("\n" + "="*40)
    # print("--- Testando o módulo 'tributavel.py' ---")
    # from src.tributavel import Tributavel
    # help(Tributavel)

