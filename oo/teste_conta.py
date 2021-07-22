def cria_conta(numero, titular, saldo, limite):
    """Cria conta de usuário.

    Args:
        conta: Dicionário com o numero, titular, saldo e limite.

    Returns:
        Dados da conta armazenado.
    """
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite
        }
    return conta

def deposita(conta, valor):
    """Adiciona valor ao saldo da conta.

    Args:
        valor: Valor a ser adicionado ao saldo.
    """
    conta['saldo'] += valor

def saca(conta, valor):
    """Subtrai valor ao saldo da conta.

    Args:
        valor: Valor a ser subtraído.
    """
    conta['saldo'] -= valor

def extrato(conta):
    """Imprime as informções sobre o saldo da conta.
    """
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))
