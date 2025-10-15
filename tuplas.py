# Tupla - conjunto de dados
# Criando uma tupla  - representado por parênteses ()
# o range sempre cria uma lista numérica - range(0,4)
# a tupla é imutável 

frutas = ('banana','uva','morango','acerola')

print(type(frutas))

print(frutas)

frutas[2] = 'manga' # aqui teremos um erro, já que ela é imutável


print(frutas[2])

# EXIBIR TODAS AS FRUTAS

for item in frutas:
    print(item)

