tupla_string = 'daiane', 'vinicius', 'rafael', 'joao', 'dani', 'jheni'

total = 0

for palavras in tupla_string:
    if len(palavras) > 5:
        total+=1
        print(f'As palavras: {palavras}')

print(f'Foi um total de {total} com caracteres maior que 5')

