tupla = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
tupla_pares = []

for n in tupla:
    if n%2==0:
        tupla_pares.append(n)

print(tuple(tupla_pares))