saldo = 50
limite = 500
extrato = ''
numero_saques = 0

while True:

    opcao = int(input("""Digite a opção desejada:
[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair """))

    if opcao == 0:
        valor = float(input('Digite o valor que deseja depositar: '))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor}'

        else:
            print('Valor informado inválido.')
    
    elif opcao == 1:
        valor = float(input('Digite o valor que deseja sacar: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques == 3

        if excedeu_saldo:
            print('Operação falhou! Não tem saldo suficiente!')

        elif excedeu_limite:
            print('Operação falhou! Ultrapassou limite de saques!')

        elif excedeu_saques:
            print('Operação falhou! Ultrapassado o limite de saques diarios!')
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor}'
            numero_saques += 1
        
        else:
            print('Operação inválida.')
    
    elif opcao == 2:
        print('EXTRATO')
        if not extrato:
            print('Não foram encontradas movimentações')
        else:
            print(extrato)
        print(f'\nSaldo: R$ {saldo}')
        print('==========================')

    elif opcao == 3:
        break


    else:
        print('Opção inválida!!!!!!!')

