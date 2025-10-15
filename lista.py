# criando uma lista - representada por colchetes []

numeros = [3, 5, 8, 10, 14]

#print(type(numeros))

print(numeros)

numeros[2] = 15 # alterando o valor do índice 2

# EXIBIR TODOS OS NÚMEROS

for item in numeros:
    print(item)

# INSERINDO VALORES NA LISTA

numeros.append(23)
print(numeros)

# ADICIONANDO ITEM EM QUALQUER LUGAR

numeros.insert(2,90)
print(numeros) # inserindo o valor 90 no indice 2

# REMOVENDO ITEM DA LISTA

numeros.pop() # remove o item do final da lista ou item específico passando o indice dentro dos parênteses
print(numeros)




