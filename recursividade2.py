# Função que irá somar valores
def soma_ate(n):
    print(f'Entrando na soma_ate({n})')
    if n == 1: # caso base:  se n for igual a 1 devolve 1
        print('-> caso base! Retornando 1')
        return 1
    resultado = n + soma_ate(n-1)
    print(f'<- Retornando {n} + ... = {resultado}')

    return resultado
    #return n + soma_ate(n - 1) # caso recursivo: n + soma dos anteriores

print(soma_ate(3)) 

# pesquisar o calculo de fatorial utilizando recursividade 

