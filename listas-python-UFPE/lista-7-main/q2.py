def porcentagem_inicial(anos_trabalhados, idade):
    return (anos_trabalhados/idade) * 100

def porcentagem_final(anos_trabalhados, idade, empresa_antiga):
    p_inicial = porcentagem_inicial(anos_trabalhados, idade)
    p_final = 0
    # empresas_rivais; 0: mais forte, 1: intermediaria, 2: mais fraca
    if idade >= 50 and p_inicial >= 30:
        if empresa_antiga == empresas_rivais[0]:
            p_final = p_inicial + 0.15*p_inicial

        elif empresa_antiga == empresas_rivais[1]:
            p_final = p_inicial + 0.1*p_inicial

        elif empresa_antiga == empresas_rivais[2]:
            p_final = p_inicial + 0.05*p_inicial

    elif idade <= 30 and p_inicial >= 40:
        if empresa_antiga == empresas_rivais[0]:
            p_final = p_inicial + 0.30*p_inicial

        elif empresa_antiga == empresas_rivais[1]:
            p_final = p_inicial + 0.25*p_inicial

        elif empresa_antiga == empresas_rivais[2]:
            p_final = p_inicial + 0.20*p_inicial

    elif p_inicial > 20:
        if empresa_antiga == empresas_rivais[0]:
            p_final = p_inicial + 0.1*p_inicial

        elif empresa_antiga == empresas_rivais[1]:
            p_final = p_inicial + 0.05*p_inicial

        elif empresa_antiga == empresas_rivais[2]:
            p_final = p_inicial + 0.03*p_inicial
    else:
        p_final = p_inicial
        
    return int(p_final)

def organizar_candidatos():
    dicionario = {}
    candidato = {}

    while True:
        try:
            candidato["nome"], candidato["idade"], candidato["empresa antiga"], candidato["tempo na empresa antiga"] = input().split(" ")
        except EOFError:
            return dicionario

        # caso o candidato já tenha sido avaliado:
        if candidato["nome"] in dicionario:
            print("{} ja esta participando da avaliacao!".format(candidato["nome"]))
            continue

        # caso o candidato não esteja nas empresas rivais:
        if candidato["empresa antiga"] not in empresas_rivais:
            print("Nao ha ligacoes entre {} e as empresas concorrentes, prossiga tranquilamente com a entrevista.".format(candidato["nome"]))

        else:   # caso ele esteja:
            dicionario[candidato["nome"]] = [candidato["idade"], candidato["empresa antiga"], candidato["tempo na empresa antiga"], porcentagem_final(int(candidato["tempo na empresa antiga"]), int(candidato["idade"]), candidato["empresa antiga"])]

def printar(espioes):
    print(f"[ALERTA]! A SEGUIR UMA LISTA DOS POSSIVEIS ESPIOES")

    for candidato, atributos in espioes.items():
        print("{}:".format(candidato))
        print("- Idade: {}".format(atributos[0]))
        print("- Antiga corporacao: {}".format(atributos[1]))
        print("- Anos trabalhos: {}".format(atributos[2]))
        print("- Probabilidade de ser espiao: {}%".format(atributos[3]))

empresas_rivais = [input(), input(), input()]

possiveis_espioes = organizar_candidatos()
printar(possiveis_espioes)