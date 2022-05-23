def velocidade_final(razao, repeticoes):
    if repeticoes == 0:
        return 0
    else:
        return razao + velocidade_final(razao, repeticoes - 1)
    
nome = input()
velocidade = int(input())
nome_da_pista = input()
moedas_coletadas = int(input())
relacoes = ["Mario Kart Stadium", 3, "Bowsers Castle", 4, "Moo Moo Meadows", 5, "Yoshi Valley", 6, "Rainbow Road", 7]

velocidade += velocidade_final(relacoes[relacoes.index(nome_da_pista) + 1], moedas_coletadas)
print(f"Correndo na pista {nome_da_pista}, {nome} coletou {moedas_coletadas} moedas e terminou a corrida na incrivel velocidade de {velocidade} km/h.")