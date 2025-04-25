#!/usr/bin/env python3

# Import necessary modules
import sys
import os

# Add the parent directory to the Python path to allow module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './src/')))

from conta import *
from funcionarios import *

# Main execution block
if __name__ == '__main__':
    c = Conta('123-4', 'Joao', 1000.0)
    cc = ContaCorrente('123-5', 'José', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)
    adc = AtualizadorDeContas(0.01)
    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)
    print('Saldo total: {}'.format(adc._saldo_total))