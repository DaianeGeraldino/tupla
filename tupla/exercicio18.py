parar = True
tupla = []
notas = []

while parar:
    notas.append(int(input("Digite as notas dos alunos ")))

    cont = int((input("Digite 1 para parar e 2 para continuar ")))

    if cont == 1:
        parar=False 

for nota in notas:
    tupla.append(nota)

nota_aluno = tuple(tupla)
print(sorted(nota_aluno))