# AND = para ser true tudo tem que ser true
# OR = para ser ture apenas um tem que ser true

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)


saldo = 1000
saque = 200 
limite = 100
conta_especial = True

saldo >= saque and saque <= limite

saldo >= saque or saque <= limite

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
