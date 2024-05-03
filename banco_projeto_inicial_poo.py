class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.conta = Conta()

    def __str__(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}'


class Conta:
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def deposito(self, valor):
        self.saldo += valor
        self.extrato.append(f'Depósito: +{valor}')

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f'Saque: -{valor}')
        else:
            print('Saldo insuficiente.')

    def ver_extrato(self):
        print('Extrato:')
        for transacao in self.extrato:
            print(transacao)
        print(f'Saldo atual: {self.saldo}')


class Banco:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def ver_clientes(self):
        print('Lista de Clientes:')
        for cliente in self.clientes:
            print(cliente)


# Testando o programa
banco = Banco()

# Cadastrando clientes
cliente1 = Cliente("João", "111.222.333-44")
cliente2 = Cliente("Maria", "222.333.444-55")

banco.cadastrar_cliente(cliente1)
banco.cadastrar_cliente(cliente2)

# Realizando transações
cliente1.conta.deposito(1000)
cliente1.conta.saque(500)
cliente1.conta.ver_extrato()

cliente2.conta.deposito(1500)
cliente2.conta.ver_extrato()

# Mostrando clientes cadastrados
banco.ver_clientes()
