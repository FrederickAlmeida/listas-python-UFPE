passos = []             # guardar os passos nessa lista
condicao = True

while condicao:
  passo = input()
  if passo == "FIM":    # caso o passo seja igual a FIM, então devermos sair do loop, caso contrário iremos anexar o elemento à lista
    condicao = False
  else:
    passos.append(passo)

print(f"Olá seguimores! O primeiro passo da dancinha é {passos[0]}")
print(f"Depois, a gente faz o {passos[1]} e {passos[2]}")
print(f"Temos ainda mais {len(passos) - 3} passos pra aprender!")
print(f"Por último, vamos fazer o {passos[-1]}")