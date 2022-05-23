rodadas = int(input())

def qtd_zumbis(n_kills, n_vivos):
    qtd_inimigos = (10*rodada + n_kills) - n_vivos
    return print(f"Haverá {qtd_inimigos} inimigos na rodada {rodada}")

for rodada in range(1, rodadas+1):
    if rodada == 1:
        qtd_zumbis(0, 0)
    else:
        auxiliar = input().split(" - ")
        qtd_zumbis(int(auxiliar[0]), int(auxiliar[1]))