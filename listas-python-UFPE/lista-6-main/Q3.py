def ispanlindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    elif palavra[-1] == "a":
        return ispanlindromo(palavra[0:-1])
    elif palavra[-1] != "a":
        return False

pistas = int(input())
mensagem = ""

for n in range(pistas):
    pista = input()
    if ispanlindromo(pista) == False:
        mensagem = "Essa não!!! Estou na direção errada."
        break

if mensagem != "Essa não!!! Estou na direção errada.":
    mensagem = "ACHEI!!! Peach, estou a caminho."

print(mensagem)