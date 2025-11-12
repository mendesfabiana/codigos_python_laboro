valor = 50

def mensagem():
    global valor # declara que estamos usando a variável global 

    print(f'Exibindo a variável valor: {valor}')

    valor = valor + 10
    print(f'O valor da variavel atualizada: {valor}')

# chamando do função
mensagem()