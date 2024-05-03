usuarios = []
AGENCIA = '007'
saldo = 10
limite = 500
numero_saques = 0
extrato = ''
lista_cpf = []
contas = []

def menu():
    print(f"""\n-----------------------------
------- BANCO DO POVO ------- 
-----------------------------
Selecione a operação desejada:

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Nova conta
[5] - Listar contas
[6] - Novo usuário
[0] - Sair

""")

def cadastrar_cliente():
    global usuarios, lista_cpf
    cpf = input('Informe o CPF: ')
    if cpf in lista_cpf:
        print('CPF já registrado')
    else:
        nome = input('Informe o nome completo: ')
        data_nascimento = input('Informe a data de nascimento (ex: 07/12/1991): ')
        endereco = input('Informe o endereço (ex: Rua Raul Veiga nº 129 - Quitandinha / Petrópolis / RJ)')

        cliente = {'CPF': cpf,
                   'Nome': nome,
                   'Data de Nascimento': data_nascimento,
                   'Endereço': endereco}

        usuarios.append(cliente)
        lista_cpf.append(cpf)

        print('Cliente cadastrado com sucesso! Bem vindo ao Banco do Povo =)')

def criar_conta(agencia, numero_conta, usuarios):
    global contas, lista_cpf
    cpf = input('Informe o CPF do usuário: ')

    if cpf in lista_cpf:

        numero_conta = len(contas) + 1

        nova_conta = {
            'Agência ': agencia,
            'Número da conta ': numero_conta,
            'CPF Titular ': cpf,
            'Saldo ': 0

        }

        contas.append(nova_conta)

        print(f'Conta criada com sucesso! Numero da conta: {numero_conta}')
    
    else:
        print('CPF não registrado.')


def depositar(saldo, valor):
    global extrato
    if valor > 0:
        saldo += valor
        extrato += f'Deposito: R$ {valor}\n'
        print('Depósito efetuado com sucesso!')
    else:
        print('Operação falhou! Valor informado é inválido')
    
    return saldo, extrato

def saque(saldo, valor): 
    global extrato, numero_saques
    if valor <= 0:
        print('Operação falhou! Valor inválido.')
        return saldo, extrato

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques == 3

    if excedeu_saldo:
        print('Operação falhou! Não tem saldo suficiente!')

    elif excedeu_limite:
        print('Operação falhou! Ultrapassou limite de saques!')

    elif excedeu_saques:
        print('Operação falhou! Ultrapassado o limite de saques diários!')
        
    else:
        saldo -= valor
        extrato += f'Saque: R$ {valor}\n'
        numero_saques += 1
    
    return saldo, extrato


def exibir_extrato(): 
    global saldo
    global extrato
    print('EXTRATO')
    if not extrato:
        print('Não foram encontradas movimentações')
    else:
        print(extrato)
    print(f'\nSaldo: R$ {saldo}')
    print('==========================')

def listar_contas():
    global contas
    for conta in contas:
        print(f' Lista de contas: {conta}')


while True:
    print(menu())
    operacao = int(input('Digite a operação desejada: '))

    if operacao == 1:
        valor_deposito = float(input('Digite o valor do depósito: '))
        saldo, extrato = depositar(saldo, valor_deposito)

    elif operacao == 2:
        valor_saque = float(input('Digite o valor que deseja sacar: '))
        saldo, extrato = saque(saldo, valor_saque)


    elif operacao == 3:
        exibir_extrato()

    elif operacao == 4:
       criar_conta(AGENCIA, len(contas) + 1, usuarios)

    elif operacao == 5:
        listar_contas()

    elif operacao == 6:
        cadastrar_cliente()

    elif operacao == 0:
        print('O Banco do povo agradece sua visita!')
        break

    else:
        print('Por favor escolha uma opção correta...')




