def rodada_jogador(cartas_usadas):
    pontuacao = 0

    while pontuacao < 17:      # enquanto a potuacao for menor que 17, continua recebendo cartas
        carta_recebida = input()
        carta = carta_recebida.split(" ")[0]
        naipe = carta_recebida.split(" ")[-1]
        
        if (carta_recebida not in cartas_usadas) and (naipe in naipes):     # caso a carta recebida ainda não tenha sido utilizada e caso ela exista
            cartas_usadas[carta_recebida] = "utilizada"
            pontuacao += cartas[carta]

        elif carta_recebida in cartas_usadas:       # caso ela já tenha sido utilizada
            print("EIEIEI, QUE ROUBO É ESSE!!!")
        
        elif carta_recebida[2] not in naipes:           # caso ela não exista
            print(f"A carta {carta_recebida} não existe, não me enganarão!")

    return pontuacao, cartas_usadas

def blackjack(pontuacao):
    if pontuacao == 21:
        print("Blackjack!")

def comparar_pontuacoes(jogador, dealer):
    if dealer > 21:
        print("AEEEEEEE, ele passou de 21, poder ir pagando chefa!!")

    elif dealer == jogador:
        print("A próxima eu levo.")

    elif dealer < jogador:
        print("O dinheiro é meu!")

    else:
        print("Perdi tudo, F.")

# observação: Caso alguma carta repetida ou inexistente seja entregue, ela não deverá ser contada como parte do jogo.
cartas = {"As": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Valete": 11, "Dama": 11, "Rei": 11}
naipes = ("ouros", "paus", "espadas", "copas")
cartas_utilizadas = {}

pontuacao_jogador, cartas_utilizadas = rodada_jogador(cartas_utilizadas)
print(f"Minha rodada acaba por aqui com {pontuacao_jogador} pontos.")

if pontuacao_jogador <= 21:     # caso a pontuação for menor ou igual a 21:
    blackjack(pontuacao_jogador)    # checar se o jogador obteve um Blackjack!

    pontuacao_dealer, cartas_utilizadas = rodada_jogador(cartas_utilizadas)
    print(f"A rodada da casa acaba por aqui com {pontuacao_dealer} pontos.")
    blackjack(pontuacao_dealer)     # checar se o dealer obteve um Blackjack!

    comparar_pontuacoes(pontuacao_jogador, pontuacao_dealer)

else:
    print("Ah não, passei do ponto!")
