num_participantes = 3
lista_participantes = []
lista_participantes_ordenados = []
lista_medias = []
lista_medias_ordenadas = []

for i in range(num_participantes):
    nome_pessoa = input()
    lista_participantes.append(nome_pessoa)
    medias = int(((int(input()) + int(input())) / 2))
    lista_medias.append(medias)

for ordem_medias in range(len(lista_medias)):
    lista_medias_ordenadas.append(max(lista_medias))
    lista_participantes_ordenados.append(lista_participantes[lista_medias.index(max(lista_medias))])
    lista_medias.remove(max(lista_medias)) # nao terá mais o ultimo numero máximo colocado, p assim poder colocar um novo máximo
    lista_participantes.remove(lista_participantes[lista_medias.index(max(lista_medias))])

print(f'1º Lugar: {(lista_participantes_ordenados[0])} com a media de views: {(lista_medias_ordenadas[0])}')
print(f'2º Lugar: {(lista_participantes_ordenados[1])} com a media de views: {(lista_medias_ordenadas[1])}')
print(f'3º Lugar: {(lista_participantes_ordenados[2])} com a media de views: {(lista_medias_ordenadas[2])}')