tupla_data = ((4,5,2005), (7,11,2000), (6,7,2006), (5,4,2023))

def ordenado(data):
    dia, mes, ano = data
    return (ano,mes,dia)

print(sorted(tupla_data, key=ordenado))
