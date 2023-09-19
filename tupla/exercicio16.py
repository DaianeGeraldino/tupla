tupla1 = (1, 2, 3, 4)
tupla2 = (5, 6, 7, 8)
tupla_soma = []

for i in range(len(tupla1)):
    soma_elementos = tupla1[i] + tupla2[i]
    tupla_soma.append(soma_elementos)

tupla_soma = tuple(tupla_soma)
print (tupla_soma)