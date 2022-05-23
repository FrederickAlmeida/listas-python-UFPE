import math
# Os atributos são: NOME[0], ATAQUE[1], DEFESA[2], ATAQUE ESPECIAL[3], VIDA[4]
jogador_1 = [input(), int(input()), int(input()), int(input())]
jogador_2 = [input(), int(input()), int(input()), int(input())]
vida_base = int(input())
vida = vida_base*100
jogador_1.append(vida)
jogador_2.append(vida)

def fibonacci(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    else:
        return fibonacci(index-1) + fibonacci(index-2)

def is_even(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def fdano(ataque, defesa_oponente, ataque_especial, rodada):
    if rodada >= 5:
        if is_even(fibonacci(rodada)):
            return ataque_especial
        else:
            return ataque - defesa_oponente
    else:
        return ataque - defesa_oponente

def lifebar(vida):
    vida_int = math.ceil(vida/(10.0 * vida_base))
    lifebarstr = ""

    for asterisco in range(vida_int):
        if (lifebarstr.count("*") + lifebarstr.count("-")) == 9:
            lifebarstr += "*"
        elif (lifebarstr.count("*") + lifebarstr.count("-")) < 9:
            lifebarstr += "* "
        else:
            break

    for hifen in range(10-vida_int):
        if (lifebarstr.count("*") + lifebarstr.count("-")) == 9:
            lifebarstr += "-"
        elif (lifebarstr.count("*") + lifebarstr.count("-")) < 9:
            lifebarstr += "- "
        else: 
            break

    return lifebarstr

def smash(dados1, dados2, rodada):
    print(f"\nROUND {rodada}:")
    if rodada % 2 == 1:
        dano = fdano(dados1[1], dados2[2], dados1[3], rodada)
        jogador_2[4] -= dano

    elif rodada % 2 == 0:
        dano = fdano(dados2[1], dados1[2], dados2[3], rodada)
        jogador_1[4] -= dano
    
    print(f"VIDA {jogador_1[0]}:")
    print(lifebar(jogador_1[4]))
    print(f"VIDA {jogador_2[0]}:")
    print(lifebar(jogador_2[4]))

    if jogador_1[4] <= 0:
        return f"O vencedor da luta foi {jogador_2[0]}"
    elif jogador_2[4] <= 0:
        return f"O vencedor da luta foi {jogador_1[0]}"

    return smash(jogador_1, jogador_2, rodada+1)

print(smash(jogador_1, jogador_2, 1))