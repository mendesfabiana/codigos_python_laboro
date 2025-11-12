agenda = dict() # inicializando um dicionario

# Função MENU

def menu():
    print('=== AGENDA ELETRÔNICA ===')
    print()
    print('1 - Inserir dados na agenda')
    print('2 - Excluir dados na agenda')
    print('3 - Consultar todos os dados da agenda')
    print('4 - Sair do sistema')

# Função inserir dados
def inserir():
        try:
            nome = input('Qual o nome do contato: ')
            agenda[nome] = int(input(f'Qual o número de {nome}: '))
            
            print('Contato inserido com sucesso!!')
            print(agenda)
        except Exception:
            print('Operação inválida. Contato não salvo')

#  Função excluir dados
def excluir(escolha):
        if escolha in agenda: # para verificar se o nome existe antes de excluir (IN)
            del agenda[escolha]
            print('Dado excluído com sucesso!!')
            print(agenda)

        else:
            print(f'O contato {escolha} não existe na agenda!!')

# Função consultar dados
def consultar():
        for chave, valor in agenda.items():
            print(f'{chave}: {valor}')


while True:
    menu()    
    resposta = int(input('Qual sua escolha: '))
    
    if resposta == 1:
        inserir()
        
    elif resposta == 2:
        print(agenda)
        escolha = input('Qual o nome do contato que você deseja excluir: ')
        excluir(escolha)
                
    elif resposta == 3:
         consultar()
        
    elif resposta == 4:
        print('Sistema encerrado!!')
        break