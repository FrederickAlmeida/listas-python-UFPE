# proibido o uso de in, de remove(), de funções de ordenação, deve-se utilizar apenas uma lista
# ordenar em ordem alfabética e não printar as que possuem letra maiúscula

hashtags = []
qntd_hashtags = int(input())
ignorar = ""

for iteration in range(qntd_hashtags):      # receber os inputs
    hashtags.append(input())

i = 0
for iteration in range(len(hashtags)):
    auxiliar = "#zzzzzzzzzzzzzzzzz"
    for hashtag in hashtags[i:]:
        pular_elemento = False
        for elemento in ignorar.split("-"):
            if hashtag == elemento:
                pular_elemento = True
        if hashtag < auxiliar and not(pular_elemento):
            auxiliar = hashtag
    hashtags.insert(i, auxiliar)
    i += 1
    ignorar += f"{auxiliar}-"

for hashtag in range(len(hashtags)//2):
    naoprintar = False
    for letra in hashtags[hashtag]:
        if letra.isupper():
            naoprintar = True
    if naoprintar == False:
        print(hashtags[hashtag])