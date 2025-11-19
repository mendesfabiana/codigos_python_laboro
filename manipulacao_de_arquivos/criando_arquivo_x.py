# Trabalhando com o modo:
# 'x' -> cria arquivo e exibe erro caso exista

try:
    arquivo = open('legumes.txt','x')

    arquivo.write('tomate\n')
    arquivo.write('alface\n')


    arquivo.close()
except Exception:
    print('Não foi possível criar o arquivo, ele já existe.')