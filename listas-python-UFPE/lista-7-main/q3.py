def comprar(numero_bolinhas, bolinhas, qtd_vendas, qtd_arrecadada):     # index das bolinhas: 0: quantidade disponível, 1: preço unitário, 2: quantidade resgatada
    if numero_bolinhas > bolinhas[0]:       # caso não haja bolinhas suficientes no estoque:
        return "Nao ha mais bolinhas disponiveis, melhor esperar um pouco.", bolinhas, [qtd_vendas, qtd_arrecadada]

    else:
        qtd_vendas += 1
        qtd_arrecadada += numero_bolinhas*1000
        bolinhas[0] -= numero_bolinhas
        bolinhas[2] += numero_bolinhas
        return f"O jogador comprou {numero_bolinhas} bolinhas por {numero_bolinhas*1000} ienes.", bolinhas, [qtd_vendas, qtd_arrecadada]

def trocar(premio, qtd_bolinhas, estoque, qtd_bolinhas_recebidas):  # index do estoque: 0: quantidade disponível, 1: preço unitário, 2: quantidade resgatada
    if (premio not in estoque) or (estoque[premio][0] <= 0):    # caso o premio nao esteja disponível
        return f"O jogador veio trocar suas bolinhas mas o premio {premio} nao esta disponivel.", estoque, qtd_bolinhas_recebidas

    elif (estoque[premio][0] > 0) and (estoque[premio][1] > qtd_bolinhas):      # caso o premio esteja disponível, mas o jogador não tenha bolinhas suficientes
        return f"O jogador precisa de mais {estoque[premio][1] - qtd_bolinhas} bolinhas para trocar por um {premio}.", estoque, qtd_bolinhas_recebidas
    
    elif (estoque[premio][0] > 0) and (estoque[premio][1] <= qtd_bolinhas):     # caso o premio esteja disponível e o jogador tenha bolinhas suficientes
        qtd_bolinhas_recebidas += estoque[premio][1]
        estoque[premio][0] -= 1
        estoque[premio][2] += 1
        estoque["bolinhas"][0] += estoque[premio][1]
        return f"O jogador trocou {estoque[premio][1]} bolinhas por um {premio}.", estoque, qtd_bolinhas_recebidas

def resgatesfeitos(tabelinha):
    resgates = 0

    for premio, infos_premio in tabelinha.items():  # somar a quantidade de resgates feito em cada um dos itens da tabela, sem incluir as bolinhas
        if premio == "bolinhas":
            continue
        else:
            resgates += infos_premio[2]

    return resgates

def premios_restantes(tabelinha):
    premios_restantes = 0

    for premio, infos_premio in tabelinha.items():   # somar a quantidade de premios restantes, sem incluir as bolinhas
        if premio == "bolinhas":
            continue
        else:
            premios_restantes += infos_premio[0]
    
    return premios_restantes

def encerrar(qtd_vendas, qtd_arrecada, bolinhas_restantes, qtd_resgates, qtd_bolinhas_recebidas, qtd_premios_restantes):
    print("\nO resumo do dia foi:")
    print(f"Arrecadado: {qtd_arrecada} ienes em {qtd_vendas} vendas;")
    print(f"Bolinhas: {bolinhas_restantes} restantes;")
    print(f"Resgates feitos: {qtd_resgates};")
    print(f"Bolinhas recebidas: {qtd_bolinhas_recebidas};")
    print(f"Premios: {qtd_premios_restantes} restantes;")
    print(f"Deu a hora, amanha tem mais!")

tabela = {"bichinho de pelucia": [10, 750, 0], "boneco articulado com armadura": [20, 1000, 0], "estatua de cena memoravel": [10, 1250, 0], "camiseta tematica": [10, 500, 0], "chaveiro": [50, 250, 0], "bolinhas": [10000, 1000, 0]}
infos_vendas = [0, 0] # 0: total de vendas, 1: total arrecadado nas vendas
bolinhas_recebidas = 0  # total de bolinhas que a loja ganhou

tem_input = True
while tem_input:    # utilizar um try except, já que teremos uma quantidade indeterminada de input
    try:
        comando = input()

    except EOFError:
        tem_input = False
        continue

    if comando == "comprar":
        mensagem, tabela["bolinhas"], infos_vendas = comprar(int(input()), tabela.get("bolinhas"), infos_vendas[0], infos_vendas[1])
        print(mensagem)

    elif comando == "trocar":
        detalhes_troca = input().split(" - ")
        mensagem, tabela, bolinhas_recebidas = trocar(detalhes_troca[0], int(detalhes_troca[1]), tabela, bolinhas_recebidas)
        print(mensagem)

    elif comando == "hora de fechar":
        encerrar(infos_vendas[0], infos_vendas[1], tabela["bolinhas"][0], resgatesfeitos(tabela), bolinhas_recebidas, premios_restantes(tabela))
        tem_input = False
