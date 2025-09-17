'''
for (etapa1; etapa2; etapa3){

}
'''
# range() não conta o valor final, ele ignora. Se quiser exibir o valor final deve acrestar + 1

# alt + z quebra a linha

# exemplo 1
for contador in range(1,11):
    print(contador, end=' ')
print('\n')
print('*' * 20)

# exemplo 2
# 0 -1 indica que o  intervalo irá de -1 em -1, isto é o passo a passo do valor inicial até o valor final.
for contador in range(10,0,-1):
    print(contador,end=' ')
    
# exemplo 3
for contador in range(0, 21, 2):
     print(contador,end=', ')
