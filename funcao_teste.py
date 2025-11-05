valor = int(input('Informe um número: '))

def par_impar(num):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'

print(f'O número {valor} é {par_impar(valor)}')

# outra forma de fazer a mesma função sem parâmetro
def parImpar():
    resposta = int(input('Informe um número: '))

    if resposta % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'
    
print(f'O número é {parImpar()}')