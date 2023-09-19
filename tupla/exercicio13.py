numeros = 2, 6, 1, 4, 3, 5
num_par = False
num = []

for numero in numeros:
    if numero%2==0:
        num.append(numero)
        num_par = True

    else:
        num_par = False

if num_par==False:
    print("A tupla possui numero impar")

else:
    print("A tupla é par")


"""
num_pares = (tuple(sorted(num)))
print(num_pares)
"""

