def isprimo(numero, nteste):
    if numero <= 2:
      if numero == 2:
        return True
      else:
        return False
    if numero % nteste == 0:
      return False
    if nteste * nteste > numero:
      return True
    return isprimo(numero, nteste+1)

def somadigitos(numero):
    if numero < 10:
        return numero
    else:
        return numero%10 + somadigitos(numero//10)

def fatorial(numero):
    if numero == 0:
        return 1
    elif numero == 1:
        return 1
    else:
        return numero * fatorial(numero-1)

condicao_labirinto = True
sequencia_erros, sequencia_acertos = 0, 0

while condicao_labirinto:
    funcao = input()

    if funcao == "Primo":
        n = int(input())
        if isprimo(n, 2):
            mensagem = f"O número {n} é primo, continue herói!"
        else:
            mensagem = "Por aqui não."

    elif funcao == "Somar":
        n = int(input())
        resultado = somadigitos(n)
        if (resultado % 2) == 0:
            mensagem = f"O número {resultado} é par, siga por aqui Link!"
        else:
            mensagem = "Por aqui não."

    elif funcao == "Fatorial":
        n = input().split(" ")
        resultado = fatorial(int(n[0]))
        if resultado == int(n[1]):
            mensagem = f"A resposta é mesmo {resultado} Link, esse caminho está certo!"
        else:
            mensagem = "Por aqui não."

    else:
        mensagem = "Por aqui não."
    
    print(mensagem)
    if mensagem == "Por aqui não.":
        sequencia_acertos = 0
        sequencia_erros += 1
    else:
        sequencia_acertos += 1
        sequencia_erros = 0
    
    if sequencia_acertos == 3:
        print("Com a sua ajuda o Link finalmente conseguiu sair do labirinto!!!")
        condicao_labirinto = False
    elif sequencia_erros == 3:
        print("Hoje não é um bom dia para o nosso herói...")
        condicao_labirinto = False