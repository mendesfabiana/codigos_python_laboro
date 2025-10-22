# no lugar de índices numéricos será textos
# um array que trabalha com chave:valor
# {chave:valor, chave:valor} -> uma chave:valor é um item

agenda = {'Maria':1234,'Pedro':4321,'Joana':9876}
contato = {'nome':'Claudio','Idade':15}

print(agenda)

print('-'*40)
print(agenda['Maria']) # mostrar o conteúdo da chave
print(f'Nome: {contato['nome']} idade: {contato["Idade"]}')

# INSERINDO DADOS NO DICIONÁRIO
# FORMA 1

agenda['José'] = 1145
print(agenda)

# FORMA 2

agenda.update({'Joana':3333}) # a função update em python pode inserir um valor ou alterar
print(agenda)


# EXCLUINDO DADOS DO DICIONÁRIO
# FORMA 1

agenda.pop('Pedro') # o pop() no dicionário precisa de um argumento 
print(agenda)

# FORMA 2

del agenda['Maria'] # mais usado
print(agenda)

agenda.clear
print(agenda)

contato.clear
print(contato)