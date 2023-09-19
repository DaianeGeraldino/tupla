num = 12, 10, 25, 32, 5
maior = True


for numeros in num:
    if numeros>10:
        maior = True
    elif numeros<10:
        maior = False

if maior:
    print("Os numeros sao maiores que 10")
else:
    print("Alguns numeros sao maior que 10")
