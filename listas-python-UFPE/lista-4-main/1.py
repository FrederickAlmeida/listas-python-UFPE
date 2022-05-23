numero_pessoasn = int(input())
lista_masculina = []
lista_feminina = []
pessoa = []

for pessoa in range(numero_pessoasn):
    pessoa = input().split(" - ")
    if pessoa[1] == "M":
        lista_masculina.append(pessoa)
    elif pessoa[1] == "F":
        lista_feminina.append(pessoa)

if len(lista_masculina) > 0 and len(lista_feminina) == 0:       # caso tenha apenas meninos
    for elemento in lista_masculina:
        print(elemento[0], end=", ")
    print("Querem cafe?")
    print(f"Serao necessarias {len(lista_masculina)} porcoes de cafe")
elif len(lista_masculina) == 0 and len(lista_feminina) > 0:     # caso tenha apenas meninas
    for elemento in lista_feminina:
        print(elemento[0], end=", ")
    print("Desculpa, so pros meninos HAHAHAHAAHHAHAHA")
    print("Nao tem meninos na lista, nao precisa fazer cafe, Neuma")
elif len(lista_masculina) > 0 and len(lista_feminina) > 0:      # caso tenha meninos e meninas
    for elemento in lista_masculina:
        print(elemento[0], end=", ")
    print("Querem cafe?")
    for elemento in lista_feminina:
        print(elemento[0], end=", ")
    print("Desculpa, so pros meninos HAHAHAHAAHHAHAHA")
    print(f"Serao necessarias {len(lista_masculina)} porcoes de cafe")