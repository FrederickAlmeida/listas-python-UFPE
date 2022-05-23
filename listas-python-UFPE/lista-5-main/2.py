frases = int(input())
letras = "abcdefghijlmnopqrstuvxz"

def palindromo(frase):
    if frase.replace(" ", "") == frase.replace(" ", "")[-1::-1]:
        return True
    else:
        return False

def panagrama(frase):
    for letra in letras:
        if letra not in frase:
            return False
    return True

def epizeuxis(frase):
  frase = frase.split(" ")
  for palavra in frase[:-1]:
    if palavra == frase[frase.index(palavra) + 1]:
      return True
  return False

for iteration in range(frases):
    frase = input()
    if palindromo(frase):
        print(f"Freddy, \"{frase}\" é um palíndromo!")
    elif panagrama(frase):
        print(f"Tenho certeza de que \"{frase}\" é um pangrama!")
    elif epizeuxis(frase):
        print(f"Freddy, Freddy, \"{frase}\" é definitivamente uma epizeuxe!")
    else:
        print(f"Essa aqui é uma pegadinha, não há nada aqui!")