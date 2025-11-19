# Trabalhando com o modo:
# 'w' -> escreve(substitui) / cria arquivo

arquivo = open('fruta.txt','w')

# verificando se um arquivo pode ser escrito
print(arquivo.writable())
arquivo.write('Maracuja\n')
arquivo.write('Acerola\n')
arquivo.write('Uva\n')
arquivo.write('Manga\n')

arquivo.close()

# criando outro arquivo

arquivo = open('verduras.txt','w')
arquivo.write('batata\n')
arquivo.write('cenoura\n')
arquivo.write('maxixe\n')
arquivo.write('quiabo\n')

arquivo.writelines(['macaxeira\n','beterraba\n']) # escrevendo várias linhas


arquivo.close()