# Escrever um algoritmo que leia um conjunto de números inteiros você deverá exibir somente os número ímpares. A leitura do valor 0 (zero) indica que o código terminou.


while True:
    num = int(input('Digite um número:'))

    if num % 2 != 0:
        print(num)
   
    if num == 0:
        break