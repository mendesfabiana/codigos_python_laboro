# CONDICIONAL 
# FORMA 1
'''
senha = 123 # inicializando a variável

while senha != 1234:
    senha = int(input('Informe sua senha: '))

print('Obrigada por usar o sistema!')
'''

# FORMA 2

tentativas = 3
while True:
    senha = input('Informe sua senha: ')

    if senha == 'aluno2' and tentativas > 0:
        print('Acesso liberado!')
        break # este comando irá encerrar o while.
    
    if tentativas > 0:
        tentativas -= 1 # está diminuindo as tentativas

    if tentativas <= 0:
        print('Sem tentativas, só lamento')
        break

    
