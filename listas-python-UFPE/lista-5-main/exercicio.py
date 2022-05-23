from random import randint
def jogo():
    num = randint(0, 100)
    acertou = False
    chute = int(input("Digite um numero inteiro no intervalo de 1 a 100: "))
    while (not acertou):
        if chute == num:
            print("Parabens, voce acertou o numero")
            acertou = True
            continue
        elif chute < num:
            print("Tente um numero maior")
        else:
            print("Tente um numero menor")
        chute = int(input("Digite um numero inteiro no intervalo de 1 a 100: "))
    print("fim de jogo")

jogo()
print("Vamos jogar denovo")
jogo()