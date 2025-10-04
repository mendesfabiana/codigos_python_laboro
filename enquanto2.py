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
    senha = input('\nInforme sua senha: ')

    if senha == 'aluno2' and tentativas > 0:
        print('\nACESSO LIBERADO!\n')
        break # este comando irá encerrar o while.
    
    if tentativas > 0:
        tentativas -= 1 # está diminuindo as tentativas
        print(f'Você possui {tentativas} tentativa(s)\n')
    if tentativas <= 0:
        print('ACESSO NEGADO!!!\n')
        break

    
