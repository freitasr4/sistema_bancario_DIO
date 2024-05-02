usuarios = []
dados_bancarios = []
conta = 0
saldo_conta = 0
saque = 0
op_saldo = 0
total_saque = 0
LIMITE_SAQUE = 0
AGENCIA = '0001'
historico = ''
cpf_usuario_atual = None

def menu():
    print(f"""\n-----------------------------
------- BANCO DO POVO ------- 
-----------------------------
Selecione a operação desejada:

[1] - Cadastrar usuário
[2] - Abrir conta corrente
[3] - Depósito
[4] - Saque
[5] - Visualizar extrato
[6] - Listar contas
[0] - Sair

""")

def cadastro_usuario(nome, data_nascimento, cpf, endereco):
    global usuarios, cpf_usuario_atual
    cpf_usuario_atual = cpf
    usuarios.append({
        'Nome': nome,
        'Data Nascimento': data_nascimento,
        'Cpf': cpf,
        'Endereço': endereco,
    })
    print('Usuário cadastrado com sucesso.\n')

def criar_conta_corrente():
    global dados_bancarios, conta, AGENCIA, cpf_usuario_atual
    conta += 1
    dados_bancarios.append({
        'Agencia': AGENCIA,
        'Conta corrente': conta,
        'Usuário': cpf_usuario_atual
    })
    print('Conta corrente aberta com sucesso.\n')

def depositar(valor, extrato):
    global saldo_conta
    if valor <= 0:
        print("Valor de depósito inválido.")
        return extrato
        
    saldo_conta += valor
    extrato = f'-------------------------\nÚltimo depósito: R$ {valor}\nSaldo da conta: R$ {saldo_conta}'
    return extrato

def sacar(valor_saque, extrato, numero_saques):
    global LIMITE_SAQUE, saldo_conta
    
    if valor_saque <= 0:
        print("Valor de saque inválido.")
        return extrato
    
    if valor_saque > saldo_conta:
        print("Saldo insuficiente.")
        return extrato
    
    if valor_saque > 500:
        print("Limite de saque excedido (máx. R$500).")
        return extrato
    
    if LIMITE_SAQUE >= 3:
        print("Limite de saque diário excedido.")
        return extrato
    
    LIMITE_SAQUE += 1
    saldo_conta -= valor_saque
    extrato = f'-------------------------\nValor sacado: R$ {valor_saque}\nSaldo da conta: R$ {saldo_conta}'
    return extrato

def visualizar_historico(saldo, comprovante):
    print(comprovante)
    print(f'\nSaldo atual: R${saldo}')

def contas_criadas(dados):
    for dado in dados:
        print('------------Contas-----------')
        print(f'Agência: {dado["Agencia"]}')
        print(f'C/C: {dado["Conta corrente"]}')
        print(f'Usuário: {dado["Usuário"]}')
        print()

while True:
    menu()
    operacao = int(input('Operação: '))

    if operacao == 1:
        saldo_conta, dados_bancarios = 0, []
        nome_usuario = input('Nome completo: ')
        nascimento = input('Data nascimento - (Ex: 15/05/1999): ')
        cpf_usuario = int(input('CPF: '))
        
        for usuario in usuarios:
            if cpf_usuario == usuario['Cpf']:
                print('\nCPF inválido!\nPor favor insira o CPF correto...')
                cpf_usuario = int(input('CPF: '))
                break
        
        endereco_usuario = input('Endereço - (Ex: RUA RAUL VEIGA, Bairro QUITANDINHA, 25652 - Petrópolis / RJ): ')
        cadastro_usuario(nome_usuario, nascimento, cpf_usuario, endereco_usuario)
        
    elif operacao == 2:
        criar_conta_corrente()
        
    elif operacao == 3:
        deposito = float(input('Valor do depósito:\nR$ '))
        historico = depositar(deposito, historico)
        
    elif operacao == 4:
        saque = float(input('Valor de saque:\nR$ '))
        op_saldo = saldo_conta
        historico = sacar(saque, historico, LIMITE_SAQUE)
        
    elif operacao == 5:
        visualizar_historico(saldo_conta, comprovante=historico)
    
    elif operacao == 6:
        contas_criadas(dados_bancarios)

    else:
        print('O Banco do Povo agradece sua visita!')
        break
