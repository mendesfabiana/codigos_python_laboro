# Vamos abrir um arquivo

'''
r -> modo de leitura
'''
# abrindo um arquivo em modo de leitura
arquivo = open('./fruta.txt','r')

# verificando se um arquivo pode ser lido

print(arquivo.readable()) # como saber se um arquivo pode ser lido

#print(arquivo.read()) # Lendo o conteúdo de um arquivo

# Lendo apenas uma linha do arquivo
#print(arquivo.readline())

# Lendo várias linhas
resultado = arquivo.readlines()
print(resultado[3])

arquivo.close() # fechando arquivo
