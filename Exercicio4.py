"""
[1] -

a = [1, 0, 5, -2, -5, 7]
print(a)

soma = a[0] + a[1] + a[5]
print(f"soma: {soma}")

a[4] = 100
print(a)


[2] -

lista = [1, 2, 3, 4, 5, 6]
print (lista)


[3]-


[4]-

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9] # armazenando em vetor numeros reais

x = int(input('Pos X: '))
y = int(input('Pos Y: '))

soma = lista[x] + lista[y]
print(soma)



[5]-

par = 0
imp = 0
for i in lista:
    if i % 2 == 0:
        par = par + 1
    else:
        imp = imp + 1
print(par)
print(imp)


[6]-

lista = [1, 2, 3, 4, 5, 6]
print(min(lista))
print(max(lista))

[7]-

vetor = []
for i in range(0, 4, 1):
    vetor.append(input('Numero:'))
print(i)
print(max(vetor[i]))
print(vetor)

[8] -

vetor = [1, 2, 3, 4]
print(vetor)
print(vetor[::-1]) #utilizando slicing

[9]-

vetor = []
for i in range(0, 6, 1):
    num = int(input(":"))
    if num % 2 == 0:
        vetor.append(num)
print(vetor)
print(vetor[::-1])


[10]

notas = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 5, 6, 4, 2]
print(notas)
print(sum(notas))
print((sum(notas)/15))

#ou

vetor = []

for i in range(0, 4, 1):
    vetor.append(int(input('Numero:')))
print(sum(vetor))
print((sum(vetor)/i))

[11] -
somaPositivo = 0
somaNegativo = 0
vetor = []

for i in range(0, 10, 1):

    num = (int(input('num:')))
    vetor.append(num)

for num in vetor:
    if num < 0:
        somaNegativo = somaNegativo - num
    else:
        somaPositivo = somaPositivo + num
print(vetor)
print(somaNegativo)
print(somaPositivo)


[12] -
tupla = []
for i in range(1, 6, 1):
    vetor = int(input('Num:'))
    tupla.append(vetor)
print(tupla)
print(max(tupla))
print(min(tupla))
print((sum(tupla)/i))

[13] -

[14] - Função count retorna quantas vezes um elemente aparece dentro de uma lista
vetor = [1, 1, 2, 3, 4, 5, 5]
repetidos = []
for i in vetor: # para cada valor em vetor[]
    if vetor.count(i) > 1 and i not in repetidos: # se o numero de valores dentro do vetor for maior que 1
        repetidos.append(i)  # e valor n esta contido mais que uma vez dentro da lista, add em repetidos
print(repetidos)
print(vetor.count(i))

[15] -
vetor = []
rep = []
for i in range(1, 21, 1):
    valor = int(input('entrada: '))
    vetor.append(valor)
print(vetor)
for i in vetor:
    if vetor.count(i) > 1 and i not in rep:
        vetor.pop(i)
print(vetor)

[16] -

vetor = []

print("Inicie preenchendo com 5 valores reais")
for i in range(5):
    valor = float(input('Valor:')) # Preenchendo vetor
    vetor.append(valor)

codigo = int(input('\n!!Codigo inteiro!!:'))
vetor.append(codigo)

if vetor[5] == 0:
    print('Codigo Encerrado!')
elif vetor[5] == 1:
    print(vetor[::1])
elif vetor[5] == 2:
    print(vetor[::-1])
else:
    print("Codigo invalido")

[17] -

matriz = [[1, 2, 3, -7], [4, 11, 6, -9], [-4, -2, 3, -10], [2, 18, 4 , 17]]
maior = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            maior = maior + 1
            print(matriz[i][j])
print(maior)

[18] -
matriz = [[], [], [], [], []]
y = 0
while y <= 16:
    for x in range(0, 5):
        matriz[x].insert(1, 0)
        y +=1
for z in range(0, 5):
    matriz[z].insert(z, 1)
print(matriz)

[19] - matriz = [[], [], [], []]

for indice_linha in range(4):
    for indice_coluna in range(4):
        matriz[indice_linha].append(indice_linha*indice_coluna)

print(matriz)

[20]

matriz = [[1, 2, 2, 3], [5, 6, 8, 9], [10, 2, 12, 13], [19, 15, 16, 10]]
maior = 0
for linha in range(4):
    for coluna in range(4):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
            print(matriz[linha][coluna])

"""



