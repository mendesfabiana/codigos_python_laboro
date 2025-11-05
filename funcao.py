# A função tem quatro tipos de usos
# MODO 1: Função sem parâmetro e sem retorno
def menu():
    print('=== MENU DO SISTEMA ===')
    print()
    print('1 - Consultar')
    print('2 - Inserir')
    print('3 - Excluir')
    print()
# chamando a função
menu()

# MODO 2: Função com parâmetro e sem retorno
def somar(num1, num2):
    print(f'A soma é {num1 + num2}')

# chamando a função
somar(4,5)

# MODO 3: Função sem parâmetro e com retorno
def dobro():
    valor = int(input('Informe um valor numérico: '))
    return valor * 2

# chamando a função
print(f'O dobro é {dobro()}')

# MODO 4: Função com parâmetro e com retorno
def triplo(valor):
    return valor * 3

# chamando a função
print(f'O triplo do valor é {triplo(8)}')

# chamando a função com valor dinâmico
numero = int(input('informe um valor: '))
print(f'O triplo do valor é {triplo(numero)}')

