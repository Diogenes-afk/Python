"""
[1] - for i in range(0, 10, 3):
      print(i)

[2] -
    //for
    for i in range(1, 101, 1):
      print(i)

      //While
      num = 0
          while num <=100:
              print(num)
              num = num +1

[3] -
    num = 10
    while num > 0:
        print(num)
        num = num - 1
        if num == 0:
            print("FIM!")
            break

[4] -
    num = 0
while num <= 100_000:
    num = num + 1_000
    print(num)
    if num == 100_000:
        break

[5] - soma = 0
for num in range(0, 10, 1):
    numero = int(input("Numero: "))
    soma = soma + numero
print(f"Soma: {soma}")

[6] - soma = 0
for num in range(0, 10, 1):
    numero = int(input("Numero: "))
    soma = soma + numero
    avg = soma/10
print(f"Media: {avg}")

[7] - soma = 0
media = 0
for i in range(1, 11, 1):
    num = int(input("Num:"))
    if num >= 0:
        soma = soma + num
        media = soma/10
    print(media)


[8] -
maior = 0
menor = 0

for i in range(0, 10, 1):

    num = int(input('Numero:'))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f"Maior:{maior}")
print(f"Menor:{menor}")


[9] -
soma = 0

for i in range(1, 50, 1):
    if i % 2 == 0:
     soma = soma + i
print(soma)
print(i)

[10] -
num = 20
for i in range(0, num, 1):
    if i >= 0:
        print(i)
    else:
        print("Numero Invalido")

[12] -
num = 20
for i in range(num, 0, -1):
    if i >= 0:
        print(i)
    else:
        print("Numero Invalido")

[15]-
num = 20
if num % 2 == 0:
    for i in range(0, num, 2):
        print(i)

[16]-
num = 23
for i in range(num, 1, -2):
    print(i)

"""













