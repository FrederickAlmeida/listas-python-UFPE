import math

viajante = []
viajante.append(input())        # nome
viajante.append(int(input()))   # vida máxima

estacao_partida, estacao_destino, estacao_proxima = "", "", ""
acontecimento = [] # evento, descricao, quantidade

tabela_armas = ["Revolver", [6, 2, 1], "Bastard", [30, 3, 15], "Duplet", [2, 5, 2], "VSV", [21, 12, 3], "Kalash", [30, 20, 5], "", [0, 0]] # nome, municao, dano
tabela_monstros = ["Lurker", [1, 2], "Nosalis", [2, 5], "Spiderbug", [4, 1], "Watcher", [5, 4], "Librarian", [10, 20]] # ataque, vida; Lu, N, S, W, Li

def roubo(descricao):
    if descricao == "arma":
        arma[0] = ""
    elif descricao == "municao":
        arma[2] = int(arma[2]) - tabela_armas[tabela_armas.index(arma[0]) + 1][0]
    return arma[0], arma[2]

def combate(monstro, quantidade):
    ataque = [0, 0] # viajante, monstros
    ataque[0] = tabela_armas[tabela_armas.index(arma[0]) + 1][1]
    quantidade = float(quantidade)
    vida[1] = tabela_monstros[tabela_monstros.index(monstro) + 1][1] * quantidade
    condicoes = True

    while condicoes:
        if arma[0] == "":   # caso o viajante esteja sem arma
            condicao, condicoes = False, False
            return condicao, f"{viajante[0]} ficou indefeso e foi devorado pelos montros! O que restou ficou no túnel para {estacao_proxima}", vida[0]

        if int(arma[2]) <= 0:  # caso a municao acabe
            condicao = False
            return condicao, f"A bala faltou quando {viajante[0]} mais precisava, a caminho de {estacao_proxima}", vida[0]
    
        vida[1] -= tabela_armas[tabela_armas.index(arma[0]) + 1][1] # jogador causa dano nos monstros
        arma[2] = int(arma[2]) - tabela_armas[tabela_armas.index(arma[0]) + 1][2]   # diminuir a munição
        quantidade = math.ceil(vida[1] / tabela_monstros[tabela_monstros.index(monstro) + 1][1]) # checar quantos monstros ainda estão vivos
        ataque[1] = tabela_monstros[tabela_monstros.index(monstro) + 1][0] * quantidade # dano dos monstros
        if quantidade > 0:
            vida[0] -= ataque[1]    # mosntros atacam o viajante

        elif vida[0] <= 0:    # caso o jogador perca por ficar sem vida
            condicao = False
            return condicao, f"{viajante[0]} lutou bravamente, mas o metrô o derrotou a caminho de {estacao_proxima}", vida[0]

        elif vida[1] <= 0:  # caso os monstros sejam mortos
            condicao = True
            return condicao, "", vida[0]

condicao = True
while condicao:
    estacao_partida = input()
    estacao_destino = input()
    if estacao_destino == estacao_partida:
        print(f"{viajante[0]} terminou sua jornada em {estacao_destino}")
        condicao = False
        continue
    
    arma = input().split(" ")
    condicao_estacaoproxima = True
    vida = [viajante[1], 0]
    while condicao_estacaoproxima and condicao:
        estacao_proxima = input()

        acontecimento = input().split(" ")
        if acontecimento[0] == "roubo":
            arma[0], arma[2] = roubo(acontecimento[1])

        elif acontecimento[0] == "combate":
            condicao, mensagem, vida[0] = combate(acontecimento[1], int(acontecimento[2]))
            if mensagem != "":
                print(mensagem)

        if (estacao_proxima == estacao_partida) and condicao:
            print(f"{viajante[0]} ficou com muito medo e voltou para {estacao_partida}")
            condicao = False
            condicao_estacaoproxima = False
            continue

        if estacao_proxima == estacao_destino and condicao:
            print(f"{viajante[0]} chegou em segurança em {estacao_destino}")
            condicao_estacaoproxima = False
