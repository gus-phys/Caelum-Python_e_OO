#!/usr/bin/env python3

from src import conta, funcionarios

# Main execution block
if __name__ == '__main__':
    c = conta.Conta('123-4', 'Joao', 1000.0)
    cc = conta.ContaCorrente('123-5', 'José', 1000.0)
    cp = conta.ContaPoupanca('123-6', 'Maria', 1000.0)
    adc = conta.AtualizadorDeContas(0.01)
    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)
    print('Saldo total: {}'.format(adc._saldo_total))