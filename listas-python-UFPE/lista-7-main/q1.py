def coletar_input(n1, n2, n3, n4, n5):
    return [n1, n2, n3, n4, n5]

def dicionario(lista_animais):
    dic = {}
    i = 1

    for animal in lista_animais:
        if (i + 1) < 9:
            dic[animal] = ["0" + str(i), "0" + str(i+1), "0" + str(i+2), "0" + str(i+3)]
        elif i == 9:
            dic[animal] = ["0" + str(i), str(i+1), str(i+2), str(i+3)]
        elif animal == "vaca":
            dic[animal] = [str(i), str(i+1), str(i+2), "00"]
        else:
            dic[animal] = [str(i), str(i+1), str(i+2), str(i+3)]
        i += 4
    
    return dic

def aposta(lista_n_sorteados):
    for numero_sorteado in lista_n_sorteados:
        for numero_apostado in tabela[bicho_apostado]:
            if numero_apostado in numero_sorteado:
                return True
    
    return False

def resultado(resultado):
    if resultado == True:
        return f"Parabens!!! Voce conseguiu ganhar {valor_apostado * 18} reais no jogo!!!"
    else:
        return f"Infelizmente nao foi dessa vez... Zeca pagodinho que acabou ganhando"

animais = ["avestruz", "aguia", "burro", "borboleta", "cachorro", "cabra", "carneiro", "camelo", "cobra", "coelho", "cavalo", "elefante", "galo", "gato", "jacare", "leao", "macaco", "porco", "pavao", "peru", "touro", "tigre", "urso", "veado", "vaca"]

tabela = dicionario(animais)
numeros_sorteados = coletar_input(input(), input(), input(), input(), input())

bicho_apostado = input()
valor_apostado = int(input())

print(resultado(aposta(numeros_sorteados)))