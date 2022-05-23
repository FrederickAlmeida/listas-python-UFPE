def busca_binaria(objetos, somar_index):
    objeto_desejado = "Ghost Potrificationizer - E. Gadd"
    meio_da_lista = len(objetos) // 2

    if len(objetos) == 1 and objetos[0] != objeto_desejado:
        return "Mamma mia! Só Mario poderá me salvar agora!"
    
    elif objetos[meio_da_lista] == objeto_desejado:
        return meio_da_lista + somar_index
    
    elif objeto_desejado > objetos[meio_da_lista]:
        return busca_binaria(objetos[meio_da_lista:], somar_index + meio_da_lista)
    
    elif objeto_desejado < objetos[meio_da_lista]:
        return busca_binaria(objetos[:meio_da_lista], somar_index)
    
def calcular_poder(posicao_arma):
    if str(posicao_arma) == str(posicao_arma)[::-1]:
        return posicao_arma
    else:
        posicao_arma = posicao_arma + int(str(posicao_arma)[::-1])
        return calcular_poder(posicao_arma)

qtd_itens = int(input())
itens = []

for item in range(qtd_itens):
    itens.append(input())

index_arma = busca_binaria(itens, 1)

if index_arma == "Mamma mia! Só Mario poderá me salvar agora!":
    print(index_arma)
else:
    poder = calcular_poder(index_arma*7)
    if poder < 50:
        print("É uma catástrofe, eu tenho a arma mas só posso usá-la uma vez")
    elif poder >= 50 and poder < 100:
        print("Terei que usar a minha arma com sabedoria!")
    elif poder >= 100 and poder < 200:
        print("A arma está bem carregada, me dei bem!")
    elif poder >= 200:
        print("Aha! EU NÃO TENHO MAIS MEDO DE NADA! PODEM VIR!")