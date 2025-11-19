# contagem com recursividade
def contagem(num):
    if num >= 1:
        print(num)
        num = num - 1
        contagem(num) # chamando a própria função

contagem(10)