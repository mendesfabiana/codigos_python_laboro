# Trabalhando com o modo:
# 'a' -> (append) adiciona conteúdo no final do arquivo

# abrindo o arquivo em modo de escrita
arquivo = open('fruta.txt','a')

arquivo.write('goiaba\n')
arquivo.write('jambo\n')
arquivo.write('pitanga\n')

arquivo.close()