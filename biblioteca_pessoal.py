biblio_pes = dict()

while True:
    print('========= MINHA BIBLIOTECA PESSOAL ===========')
    print()
    print('1 - Adicionar livro')
    print('2 - Consultar livro')
    print('3 - Atualizar páginas')
    print('4 - Remover livro')
    print('5 - Listar todos os livros')
    print('6 - Contar livros')
    print('7 - Sair')

    opcao = int(input('Digite sua opcão: '))

    if opcao == 1: # adicinando livro
        livro = input('Digite o nome do livro: ')
        biblio_pes[livro] = int(input('Digite o número de páginas: '))

        print('Livro inserido com sucesso!')
    
    elif opcao == 2: #consultando o livro
        livro = input('Digite o nome do livro que você quer consultar: ')
        if livro in biblio_pes:
            print(f'O livro {livro} tem {biblio_pes[livro]} páginas')
    

    #elif opcao == 3:
        #biblio_pes.update(int(input(''))



