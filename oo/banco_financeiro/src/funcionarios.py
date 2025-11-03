import abc

# Autnenticação
class SistemaInterno:

    def login(self, obj):
        if (hasattr(obj, 'autentica')):
            obj.autentica(obj._senha)
            return True
        else:
            print('{} não é autenticável'.format(obj.__class__.__name__))
            return False

class AutenticavelMixIn:

    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False

# Funcionários
class Funcionario(abc.ABC):

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @abc.abstractmethod
    def get_bonificacao(self):
        return self._salario * 0.1

class ControleDeBonificacoes:

    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if (hasattr(obj, 'get_bonificacao')):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print('instância de {} não implementa o método get_bonificacao()'.format(obj.__class__.__name__))

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

# Tipos de funcionários
class Gerente(Funcionario, AutenticavelMixIn):

    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000

class Diretor(Funcionario, AutenticavelMixIn):

    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000

# Clientes
class Cliente(AutenticavelMixIn):

    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha
