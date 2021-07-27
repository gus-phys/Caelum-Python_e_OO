import datetime

class Historico:
    def __init__(self):
        # self.data_abertura = datetime.datetime.today()
        self.transacoes = []
        self.data = Data()

    def imprime(self):
        print("data abertura: {}".format(self.data.data_abertura))
        print("transações: ")
        for t in self.transacoes:
            print("-", t)

class Data:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.dia = self.data_abertura.day
        self.mes = self.data_abertura.month
        self.ano = self.data_abertura.year

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("deposito de {}".format(valor))

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))
            # return True

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("transferência de {} para conta"
            " {}".format(valor, destino.numero))
            return True

    def extrato(self):
        print(
        "nome: {} {} \ncpf: {} \nnumero: {} \nsaldo: {}"
        .format(self.titular.nome, self.titular.sobrenome, self.titular.cpf,
        self.numero, self.saldo)
        )
        self.historico.transacoes.append("tirou extrato - saldo de {}"
        .format(self.saldo))
