tupla = 1, 2 , 3, 4, 5, 6, 7, 8, 9
num_encontrado = False

num = int(input("Digite qual numero deseja encontrar "))

for numero in tupla:
    if numero == num:
        num_encontrado = True

if num_encontrado:
    print('Numero encontrado')

else: 
    print("NAO ENCONTRADO")
        
