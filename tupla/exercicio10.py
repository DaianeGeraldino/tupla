tupla_string = 'juliana', 'vinicius', 'joao', 'daiane'
comprimentos = []

for n in tupla_string:
    comprimento = len(n)
    comprimentos.append(comprimento)

comprimentos_tupla = tuple(comprimentos)

print("Tupla de palavras:", tupla_string)
print("Tupla de comprimentos:", comprimentos_tupla)