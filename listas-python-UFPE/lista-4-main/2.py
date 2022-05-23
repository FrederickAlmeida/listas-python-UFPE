qntd_videos = int(input())
usuarios_nome = []
usuarios_notas = []
rank_notas = []

for video in range(qntd_videos):
    usuarios_nome.append(input())
    usuarios_notas.append(int(input()))

primeiro_lugar = usuarios_nome[usuarios_notas.index(max(usuarios_notas))]    # salvar o nome do usuario com mais likes
while len(usuarios_notas) > 0:
    rank_notas.append(max(usuarios_notas))
    usuarios_notas.remove(max(usuarios_notas))

print("O numero de curtidas dos videos que vao aparecer na For You segue a ordem:")
for nota in rank_notas:
    if nota != (rank_notas[-1]):
        print(nota, end=", ")
    else:
        print(nota)

print(f"O primeiro usuario que vai aparecer na For You e {primeiro_lugar}!")