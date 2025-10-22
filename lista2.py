# 
valores = [] # criando uma lista vazia

for item in range(10,14):
    valores.append(item)
print(valores)

# PREENCHENDO UMA LISTA COM DADOS DINAMICOS

valores2 = []
while True:
    num = int(input('Informe um valor numérico qualquer - zero para encerrar: '))
    if num == 0:
        break # encerra o sistema
    else:
        valores2.append(num)
print('\nPrograma encerrado\n')
print(valores2)
print()

while True:
    print()
    apagar = int(input('Gostaria de apagar algum item da lista?\n[1] sim\n[2] não\n\nDigite a opção: '))
    if apagar == 2:
        print('Programa encerrado!!!')
        break
    if len(valores2) == 0: # len() verifica o tamanho da lista
        print('A lista está vazia')
        break
    else:
        valores2.pop()
        print(valores2)

    
