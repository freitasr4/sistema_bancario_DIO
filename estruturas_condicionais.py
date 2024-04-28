'''opcao = int(input('Informe uma opção: [1] sacar \n[2] Extrado: '))

if opcao == 1:
    valor = float(input('Informe o valor do saque: '))

elif opcao == 2:
    print('Exibindo o extrato...')

else:
    sys.exit('Opção inválida')'''

idade = int(input('Informe a sua idade: '))

if idade >= 18:
    print('Pode tirar a CNH')

else:
    print('Não pode tirar a CNH')