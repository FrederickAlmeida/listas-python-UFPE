def ordenar_cartas(dicionario):
    dic_organizado = {}
    while len(dicionario) > 0:  # enquanto houver cartas para serem ordenadas
        menor_valor = ["carta", 6]  # variavel para comparacao
        for carta,preco in dicionario.items():  # loop para descobrir a carta com o menor preço
            if preco < menor_valor[1]:
                menor_valor = [carta, preco]

        dic_organizado[menor_valor[0]] = menor_valor[1] # salvar o menor elemento no dicionario organizado
        del dicionario[menor_valor[0]]                  # remover o menor elemento do dicionario
    
    return dic_organizado

def printar(dicionario):
    for carta, preco in dicionario.items():
        print(f"{carta} - {preco}")

cartas = {}
for iteration in range(5):
    entrada = input().split(" - ")
    cartas[entrada[0]] = int(entrada[1])

cartas = ordenar_cartas(cartas)
printar(cartas)