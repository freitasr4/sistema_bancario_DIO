conta_normal = True
conta_universitaria = False
cheque_especial = 500.50


saldo = 1500.07

saque = float(input('Digite o valor a sacar: '))


if conta_normal:

    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realziado com uso de cheque especial!')
    else:
        print('Não foi possíverl efetuar o saque!')

elif conta_universitaria:
    
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')
else:
    print('Sistema não reconheceu o seu tipo de conta, entre em contato com o gerente.')