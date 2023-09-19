numeros = 2, 2, 5, 6, 7, 8, 9, 8
tupla_nova = []

for numero in numeros:
    if numero in tupla_nova:
        continue
    else:
        tupla_nova.append(numero)

num_rep = tuple(tupla_nova)
print(num_rep)