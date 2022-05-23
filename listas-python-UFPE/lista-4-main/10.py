condicao = True
liberos = []
levantadores = []
centrais = []
ponteiros = []
opostos = []
todos_jogadores = []

while condicao:
    comando = input()
    if comando == "adicionar":
        jogador = input().split(": ")
        if jogador[-1] == "Levantador":
            levantadores.append(jogador[0])
            todos_jogadores.append(jogador[0])
            if len(levantadores) == 5:
                print("Cuidado! voce ja possui 5 levantadores")

        elif jogador[-1] == "Libero":
            liberos.append(jogador[0])
            todos_jogadores.append(jogador[0])
            if len(liberos) > 2:        # caso tenha mais de 2 liberos: encerrar o codigo
                print("ERRO: liberos demais, nao temos uniformes suficientes")
                condicao = False
                continue

        elif jogador[-1] == "Central":
            centrais.append(jogador[0])
            todos_jogadores.append(jogador[0])
            if len(centrais) == 5:
                print("Cuidado! voce ja possui 5 centrais")

        elif jogador[-1] == "Ponteiro":
            ponteiros.append(jogador[0])
            todos_jogadores.append(jogador[0])
            if len(ponteiros) == 5:
                print("Cuidado! voce ja possui 5 ponteiros")

        elif jogador[-1] == "Oposto":
            opostos.append(jogador[0])
            todos_jogadores.append(jogador[0])
            if len(opostos) == 5:
                print("Cuidado! voce ja possui 5 opostos")

        if len(todos_jogadores) > 18:     # caso tenha mais de 18 jogadores: encerrar o codigo
            print("ERRO: voce estrapolou o numero de jogadores")
            condicao = False
            continue

    elif comando == "relatorio":
        print("No nosso time ja possuimos:")
        print(f"Liberos: {len(liberos)}")
        print(f"Levantadores: {len(levantadores)}")
        print(f"Ponteiros: {len(ponteiros)}")
        print(f"Centrais: {len(centrais)}")
        print(f"Opostos: {len(opostos)}")
        print(f"TOTAL: {len(todos_jogadores)}")
        
    elif comando == "nomes":
        posicao = input()
        if posicao == "Levantador" and len(levantadores) > 0:
            print("Os levantadores sao:")
            for element in levantadores:
                print(element)

        elif posicao == "Libero" and len(liberos) > 0:
            print("Os liberos sao:")
            for element in liberos:
                print(element)

        elif posicao == "Central" and len(centrais) > 0:
            print("Os centrais sao:")
            for element in centrais:
                print(element)

        elif posicao == "Ponteiro" and len(ponteiros) > 0:
            print("Os ponteiros sao:")
            for element in ponteiros:
                print(element)

        elif posicao == "Oposto" and len(opostos) > 0:
            print("Os opostos sao:")
            for element in opostos:
                print(element)
        else:
            print("Ainda nao temos jogadores nessa posicao")

    elif comando == "buscar":
        nome = input()
        if nome == "Samuel":
            if nome in todos_jogadores:
                print("Sim, Samuel, voce ja esta na lista de jogadores")
            else:
                print("Como voce pode esquecer de si mesmo? Voce nao esta na lista")
        else:
            if nome in todos_jogadores:
                print(f"Sim, {nome} esta na lista de jogadores")
            else:
                print(f"O jogador {nome} nao esta na lista de jogadores")

    elif comando == "fim":
        condicao = False

    else:
        print("***COMANDO INVALIDO***")

# se for valido
if (len(liberos) == 2) and (len(todos_jogadores) <= 18) and (len(levantadores) >= 2) and (len(centrais) >= 2) and (len(ponteiros) >= 2) and (len(opostos) >= 2):
    print(f"O Navegantes esta pronto para disputar o Estadual! Desejem sorte aos nossos {len(todos_jogadores)} jogadores!")
else:
    print(f"Quem mandou ficar perdendo tempo com TikTok... Agora o Navegantes nao conseguira jogar o estadual :(")