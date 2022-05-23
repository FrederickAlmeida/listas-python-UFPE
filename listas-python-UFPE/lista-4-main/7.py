trechos_corrigidos = []
contador_ruidosos = 0

for iteration in range(10):
    trecho = input()
    if (trecho.split(" ")[0] == "zzz" or trecho.split(" ")[0] == "tss") and (len(trecho.split(" ")) > 1) and not(trecho.split(" ")[-1] == "zzz" or trecho.split(" ")[-1] == "tss"):
        contador_ruidosos += 1
        trecho_corrigido = trecho.split(" ")[1:]
        trechos_corrigidos.append(" ".join(trecho_corrigido))
    elif (trecho.split(" ")[-1] == "zzz" or trecho.split(" ")[-1] == "tss") and (len(trecho.split(" ")) > 1) and not(trecho.split(" ")[0] == "zzz" or trecho.split(" ")[0] == "tss"):
        contador_ruidosos += 1
        trecho_corrigido = trecho.split(" ")[:-1]
        trechos_corrigidos.append(" ".join(trecho_corrigido))
    elif (trecho.split(" ")[0] == "zzz" or trecho.split(" ")[0] == "tss") and (len(trecho.split(" ")) > 1) and (trecho.split(" ")[-1] == "zzz" or trecho.split(" ")[-1] == "tss"):
        contador_ruidosos += 1
        trecho_corrigido = trecho.split(" ")[1:-1]
        trechos_corrigidos.append(" ".join(trecho_corrigido))
    elif (trecho == "zzz" or trecho == "tss"):
        contador_ruidosos += 1
    else:
        trechos_corrigidos.append(trecho)

if contador_ruidosos == 10:
    print("Eita, a legenda simplesmente inexiste! Tudo era ruido!")
elif len(trechos_corrigidos) > 0:
    print("Legenda final:\n")
    for element in trechos_corrigidos:
        print(element)

if (contador_ruidosos >= 1 and contador_ruidosos <= 4) and len(trechos_corrigidos) >= 8:
    print("\nTodo o ruido foi removido e voce mandou bem! A legenda saiu certinha. Pode subir!")
elif contador_ruidosos == 0:
    print("\nNem precisava rodar, o audio ja estava limpinho e a legenda ta nos conformes. Marca o @billyraycyrus")
elif (contador_ruidosos > 4 or len(trechos_corrigidos) < 8) and len(trechos_corrigidos) > 0:
    print("\nIh, tem alguma coisa errada com a legenda, ta estranha. Melhor dar uma verificada e regravar.")