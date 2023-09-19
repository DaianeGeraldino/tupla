
frutas = ("maçã", "banana", "laranja", "uva", "pera", "abacaxi")

fruta_procurada = input("Digite em minusculo a fruta que procura ")

if fruta_procurada in frutas:
    posicao = frutas.index(fruta_procurada)
    print(f"A fruta '{fruta_procurada}' está na posição {posicao + 1} da tupla.")
else:
    print(f"A fruta '{fruta_procurada}' não foi encontrada na tupla.")
