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
    
    # __slots__ = [
    #     '_numero', 
    #     '_titular', 
    #     '_saldo', 
    #     '_limite', 
    #     'historico'
    #     ]
    
    identificador = 1

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()

        self.identificador = Conta.identificador
        Conta.identificador += 1
        
    def __str__(self):
        return "Dados da Conta: \nNumero: {} \nTitular: {} \nSaldo: {} \nLimite: {}".format(
            self._numero,
            self._titular,
            self._saldo,
            self._limite
        )

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
        
    def atualiza(self, taxa):
        self._saldo += self._saldo*taxa
        return self._saldo

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

class ContaCorrente(Conta):
    
    def atualiza(self, taxa):
        self._saldo += self._saldo*taxa*2
        return self._saldo
        
    def deposita(self, valor):
        self._saldo += valor - 0.1

class ContaPoupanca(Conta):
    
    def atualiza(self, taxa):
        self._saldo += self._saldo*taxa*3
        return self._saldo
        
class AtualizadorDeContas:
    
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total
        
    def roda(self, conta):
        print("Saldo da Conta: {}".format(conta._saldo))
        self._saldo_total += conta.atualiza(self._selic)
        print("Saldo Final: {}".format(self._saldo_total))