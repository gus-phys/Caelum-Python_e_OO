#!/usr/bin/env python3

from src.conta import *
from src.manipulador_tributaveis import ManipuladorDeTributaveis

if __name__ == '__main__':
    banco = Banco('Banco Caelum')

    joao_silva = Cliente('João', 'Silva', '111.222.333-44')
    maria_souza = Cliente('Maria', 'Souza', '555.666.777-88')
    ana_oliveira = Cliente('Ana', 'Oliveira', '999.000.111-22')
    
    cc = ContaCorrente('123-5', 'José', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)
    ci = ContaInvestimento('123-7', 'Ana', 1000.0)

    cc_joao = ContaCorrente('223-5', joao_silva, 1000.0)
    cp_maria = ContaPoupanca('223-6', maria_souza, 1000.0)
    ci_ana = ContaInvestimento('223-7', ana_oliveira, 1000.0)

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
    
    print("\n--- Dados de uma conta ---")
    print(cc_joao)

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
    # help(Tributavel)

    print("\n" + "="*40)
    print("--- Testando try/except' ---")

    lista_valores = [-10, 10, 1000, 1000000]
    caixa_eletronico = CaixaEletronico("Banco Caelum", 10000)

    print(">>> Depósito <<<")
    for valor in lista_valores[:2]:
        caixa_eletronico.deposito(valor, cc_joao)

    caixa_eletronico.deposito(10, seguro1)  # Testando depósito em objeto não Conta

    print("\n>>> Saque <<<")
    for valor in lista_valores:
        caixa_eletronico.saque(valor, cc_joao)
        
    print("\n>>> Extrato <<<")
    cc_joao.extrato()
    print("\n>>> Histórico <<<")
    cc_joao.historico.imprime()

    # print("\n" + "="*40)
    # print("--- Testando módulo The Python Debugger ---")
    # import pdb; pdb.set_trace()
    # pdb.run('caixa_eletronico.saque(5000, seguro1)')  # Testando saque em objeto não Contaç