curso = 'PYtHon'

print(curso.upper()) #Converter tudo em maisuclo

print(curso.lower())#Converter tudo em minusculo

print(curso.title())#Primeira letra maiuscula

print(curso.strip())#Tirar os espaços em braco

print(curso.lstrip())#Tirar os espaços da esquerda

print(curso.rstrip)#Tirar os espaços da direita

print(curso.center(10, '#'))

print('.'.join(curso))

nome = 'Renan Coelho de Freitas'
idade = 32
profissao = 'Programador'
linguagem = 'Python'

print(f'Olá, meu nome é {nome}\n idade {idade}\n profissão {profissao}\n linguagem: {linguagem}')

print(nome[0])
print(nome[-1])
print(nome[:3])
print(nome[1:])
print(nome[1:4:9])
print(nome[:1])

PI = 3.14159
print(f'Valor de PI: {PI:.2f}')