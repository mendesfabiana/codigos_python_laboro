biblio_pessoal = dict()

while True:
    print()
    print('=== MINHA BIBLIOTECA ===')
    print()
    print('1. Adicionar livro')
    print('2. Consultar livro')
    print('3. Atualizar páginas')
    print('4. Remover livro')
    print('5. Listar todos os livros')
    print('6. Contar livros')
    print('7. Sair')
    print()
    opcao = int(input('Escolha uma opção: '))

    try:
        if opcao == 1:
            try:
                print()
                print('=== ADICIONAR LIVRO ===')
                print()
                livro = input('Digite o  nome do Livro: ')
                biblio_pessoal[livro] = int(input('Digite o número de páginas: '))
                print()
                print('LIVRO ADICIONADO COM SUCESSO!')
            except Exception:
                print()
                print('OPERAÇÃO INVÁLIDA!! DIGITE NOVAMENTE.')

        elif opcao == 2:
            try:
                print()
                print('===CONSULTAR LIVRO ===')
                print()
                livro = input('Digite o nome do livro: ')
                print()
                print(f'O livro {livro} tem {biblio_pessoal[livro]} páginas')   
            except Exception:
                print()
                print('OPERAÇÃO INVÁLIDA! DIGITE NOVAMENTE.')
                
        elif opcao == 3:
            print()
            print('=== ATUALIZAR LIVRO ===')
            print()
            livro = input('Digite o nome do livro: ')
            paginas = int(input('Digite o novo número de páginas: '))
            biblio_pessoal.update({livro:paginas}) 
            print()
            print('LIVRO ATUALIZADO COM SUCESSO!')
            print(f'livro {livro}: {biblio_pessoal[livro]} páginas.')
        
        elif opcao == 4:
            print()
            print('=== REMOVER LIVRO ===')
            print()
            livro = input('Digite o nome do livro a ser removido: ')
            if livro in biblio_pessoal:
                del biblio_pessoal[livro]
                print()
                print('LIVRO REMOVIDO COM SUCESSO!')
            else:
                print()
                print('LIVRO NÃO ENCONTRADO NA BIBLIOTECA!')

        elif opcao == 5:
            print()
            print('=== LIVROS NA BIBLIOTECA ===')
            print()
            for chave, valor in biblio_pessoal.items():
                print(f'- {chave}: {valor} páginas')
                if len(biblio_pessoal) == 0:
                    print('NENHUM LIVRO CADASTRADO NA BIBLIOTECA!')

        elif opcao == 6:
            print('=== TOTAL DE LIVROS ===')
            print()
            print(f'Total de livros na biblioteca: {len(biblio_pessoal)}')
            

        elif opcao == 7:    
            print()
            print('SAINDO DO SISTEMA...')
            print()
            break
    except Exception:   
        print()
        print('OPERAÇÃO INVÁLIDA! DIGITE NOVAMENTE.')
    