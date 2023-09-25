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

    # __slots__ = ['_numero', '_titular', '_saldo', '_limite', 'historico']

    identificador = 1

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()

        self.identificador = Conta.identificador
        Conta.identificador += 1

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(
            "{} - deposito de {}".format(
                datetime.datetime.today(),
                valor,
                )
            )

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(
                "{} - saque de {}".format(
                    datetime.datetime.today(),
                    valor
                    )
                )
            return True

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(
                "{} - transferência de {} para conta {}".format(
                    datetime.datetime.today(),
                    valor, 
                    destino._numero
                    )
                )
            return True

    def extrato(self):
        print(
        "nome: {} {} \ncpf: {} \nnumero: {} \nsaldo: {}"
        .format(self._titular.nome, self._titular.sobrenome, self._titular.cpf,
        self._numero, self._saldo)
        )
        self.historico.transacoes.append(
            "{} - tirou extrato - saldo de {}".format(
                datetime.datetime.today(),
                self.saldo
                )
            )
