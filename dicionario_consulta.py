alimentos = {'arroz':5.99,'café':14.00,'feijão':7.69}

'''
Dicionário
chave: valor -> item

chave - key
valor - value
item  - item
'''

print(alimentos)

# ACESSANDO APENAS AS CHAVES

for chave in alimentos.keys():
    print(chave)

# ACESSANDO APENAS OS VALORES

for valor in alimentos.values():
    print(valor)

# ACESSANDO O ITEM

for chave, valor in alimentos.items():
    print(f'{chave} : {valor}')