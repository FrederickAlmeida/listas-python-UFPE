participantes = []
medias = []

for participante in range(3):
    participantes.append(input())
    medias.append(int((int(input()) + int(input()))/2))

for colocacao in range(1, 3+1):
    print(f"{colocacao}º Lugar: {participantes[medias.index(max(medias))]} com a media de views: {max(medias)}")
    participantes.remove(participantes[medias.index(max(medias))])
    medias.remove(max(medias))