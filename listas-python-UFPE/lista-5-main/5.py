personagens = ["Sam", "Chris", "Ashley", "Jessica", "Mike", "Emily", "Matt"]
status = ["vivo", "vivo", "vivo", "vivo", "vivo", "vivo", "vivo"]
relacoes = [
    [-1, 5, 5, 5, 5, 5, 5],  # sam
    [5, -1, 6, 5, 5, 5, 5],  # chris
    [5, 6, -1, 5, 5, 5, 5],  # ashley
    [5, 5, 5, -1, 7, 4, 5],  # jessica
    [5, 5, 5, 7, -1, 3, 4],  # mike
    [5, 5, 5, 4, 3, -1, 7],  # emily
    [5, 5, 5, 5, 4, 7, -1]  # matt
]

def modificador_relacoes(nome1, nome2, valor):
    if valor == "X" and (nome1 != nome2):
        return "somar", -1
    elif valor == "O" and (nome1 != nome2):
        return "somar", 1
    elif nome1 == nome2:
        return "somar", 0
    else:
        return "substituir", int(valor)

# fase inicial
n_interacoes = int(input())
for i in range(n_interacoes):
    interacao = input().split(" ")
    if modificador_relacoes(interacao[0], interacao[2], interacao[1])[0] == "somar":
        relacoes[personagens.index(interacao[0])][personagens.index(interacao[2])] += modificador_relacoes(interacao[0], interacao[2], interacao[1])[1]
        relacoes[personagens.index(interacao[2])][personagens.index(interacao[0])] += modificador_relacoes(interacao[2], interacao[0], interacao[1])[1]
    else:
        relacoes[personagens.index(interacao[0])][personagens.index(interacao[2])] = modificador_relacoes(interacao[0], interacao[2], interacao[1])[1]
        relacoes[personagens.index(interacao[2])][personagens.index(interacao[0])] = modificador_relacoes(interacao[2], interacao[0], interacao[1])[1]

# fase 2

def analise_relacoes(nomes):
    if nomes.count(" ") >= 1:
        nomes = nomes.split(" - ")
        if status[personagens.index(nomes[0])] == "vivo" and status[personagens.index(nomes[1])] == "vivo":
            if relacoes[personagens.index(nomes[0])][personagens.index(nomes[1])] > 6:
                return "vivo", f"felizmente {nomes[1]} ajudou {nomes[0]} a escapar do Wendigo."
            else:
                return "morto", f"que pena! {nomes[1]} nao conseguiu ajudar {nomes[0]} do ataque do Wendigo."
        else:
            if status[personagens.index(nomes[0])] == "morto":
                return "morto", f"entrada invalida!!! voce so pode jogar com jogadores vivos"
            elif status[personagens.index(nomes[0])] == "vivo":
                return "vivo", f"entrada invalida!!! voce so pode jogar com jogadores vivos"
    else:
        if status[personagens.index(nomes)] == "vivo":
            soma = 0
            for numero in relacoes[personagens.index(nomes)]:
                if numero > 0:
                    soma += numero
            if (soma/6.0) > 5:
                return "vivo", f"UFA!!! foi por pouco mas {nomes} conseguiu escapar do Wendigo."
            else:
                return "morto", f"{nomes} infelizmente nao conseguiu sobreviver ao ataque do Wendigo."
        else:
            return "morto", f"entrada invalida!!! voce so pode jogar com jogadores vivos"


n_entradas = int(input())
for i in range(n_entradas):
    nome = input()
    if nome.count(" ") >= 1:
        status[personagens.index(nome.split(" - ")[0])], printar = analise_relacoes(nome)
    else:
        status[personagens.index(nome)], printar = analise_relacoes(nome)
    print(printar)

print("")
if "vivo" in status:
    print("Sobreviventes:")
    for i in personagens:
        if status[personagens.index(i)] == "vivo":
            print(i)
else:
    print("Tristemente, ninguém sobreviveu")