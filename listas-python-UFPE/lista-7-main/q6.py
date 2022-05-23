def ship(primeiro, segundo):
    for letra in primeiro[1:]:
        if letra in segundo[1:]:
            combinacao_nomes = primeiro[0:primeiro.index(letra)] + segundo[segundo.index(letra):]
            return 20, combinacao_nomes
    
    combinacao_nomes = primeiro[:len(primeiro)//2] + segundo[(len(primeiro)//2)+1:]
    return 0, combinacao_nomes

def azeitona(gostos_primeiro, gostos_segundo):
    if ("Azeitona" in gostos_primeiro) and ("Azeitona" in gostos_segundo):
        if gostos_primeiro["Azeitona"] != gostos_segundo["Azeitona"]:
            return 50

        else:
            return 0

def multiplas_respostas(gostos_primeiro, gostos_segundo, caracteristica_dada):
    somar_pontuacao = 0

    if (caracteristica_dada in gostos_primeiro) and (caracteristica_dada in gostos_segundo):
        for gosto in gostos_primeiro[caracteristica_dada]:
            if gosto in gostos_segundo[caracteristica_dada]:
                somar_pontuacao += 2
    
    return somar_pontuacao

def descobrir_signo(aniversario):
    mes = aniversario[0].split("/")[1]
    return signos[mes]

def aniversario(gostos_primeiro, gostos_segundo):
    if ("Aniversario" in gostos_primeiro) and ("Aniversario" in gostos_segundo):
        signo_primeiro = descobrir_signo(gostos_primeiro["Aniversario"])
        signo_segundo = descobrir_signo(gostos_segundo["Aniversario"])

        elemento_primeiro = elemento_signo[signo_primeiro]
        elemento_segundo = elemento_signo[signo_segundo]

        if elemento_primeiro == elemento_segundo:
            return 10
        
        elif "ar" in [elemento_primeiro, elemento_segundo] and "agua" in [elemento_primeiro, elemento_segundo]:
            return 5
        
        elif "fogo" in [elemento_primeiro, elemento_segundo] and "terra" in [elemento_primeiro, elemento_segundo]:
            return 5
        
        else:
            return 0

def caracteristica_generica(gostos_primeiro, gostos_segundo, caracteristica_dada):
    if (caracteristica_dada in gostos_primeiro) and (caracteristica_dada in gostos_segundo):
        if gostos_primeiro[caracteristica_dada] == gostos_segundo[caracteristica_dada]:
            return 3

        else:
            return 0


def calculo_final(primeiro, segundo, pontuacao):
    for caracteristica, resposta in primeiro.items():
        if caracteristica == "Azeitona":
            pontuacao += azeitona(primeiro, segundo)
        
        elif caracteristica in ["Musicas", "Series", "Filmes", "Livros"]:
            pontuacao += multiplas_respostas(primeiro, segundo, caracteristica)
        
        elif caracteristica == "Aniversario":
            pontuacao += aniversario(primeiro, segundo)
        
        else:
            pontuacao += caracteristica_generica(primeiro, segundo, caracteristica)
    
    return pontuacao


print("Digite seu nome e o nome do/da Crush:")
porcentagem_combinacao, comb_nomes = ship(input(), input())
print(f"Hmmm, estou sentindo a conexão entre vocês... {comb_nomes} é um bom ship!")

signos = {"04":"aries", "05":"touro", "06":"gemeos", "07":"cancer", "08":"leao", "09":"virgem", "10":"libra", "11":"escorpiao", "12":"sagitario", "01":"capricornio", "02":"aquario", "03":"peixes"}
elemento_signo = {"cancer":"agua", "peixes":"agua", "escorpiao":"agua", "aries":"fogo", "leao":"fogo", "sagitario":"fogo", "touro":"terra", "virgem":"terra", "capricornio":"terra", "gemeos":"ar", "libra":"ar", "aquario":"ar"}

primeira_pessoa = {}
segunda_pessoa = {}

primeira_pessoa_input = True
existir_entradas = True

while existir_entradas:
    if primeira_pessoa_input == True:
        entrada = input()
        if entrada == "---":
            primeira_pessoa_input = False
            continue

        else:
            primeira_pessoa[entrada.split(" ")[0]] = entrada.split(" ")[1:]

    else:
        try:
            entrada = input().split(" ")
            segunda_pessoa[entrada[0]] = entrada[1:]

        except EOFError:
            existir_entradas = False
            continue

porcentagem_combinacao = calculo_final(primeira_pessoa, segunda_pessoa, porcentagem_combinacao)

print(f"Vocês combinam {porcentagem_combinacao}%!")
