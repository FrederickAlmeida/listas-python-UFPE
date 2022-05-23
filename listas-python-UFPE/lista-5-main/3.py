condicao = True
vitorias = [0, 0]
luke_input = []
ursinho_input = []

def vencedor_round(luke_input, ursinho_input):
  if int(luke_input[round-1][1]) > int(ursinho_input[round-1][1]):
    return "luke"
  else:
    return "ursinho"

for i in range(5):
  luke_input.append(input().split("/"))
for i in range(5):
  ursinho_input.append(input().split("/"))

round = 1
while condicao and round <= 5:
  if vencedor_round(luke_input, ursinho_input) == "luke":
    vitorias[0] += 1
    print(f"Luke foi muito esperto, usou {luke_input[round-1][0]} e ganhou o {round}º round!")
  else:
    vitorias[1] += 1
    print(f"Inscryption nao aliviou, usou {ursinho_input[round-1][0]} e venceu o {round}º round!")

  if vitorias[0] == 3:
    print("Luke Carter ganhou na batalha de cartas e avançou de fase na sua luta para conseguir sair da cabana!")
    condicao = False
  elif vitorias[1] == 3:
    print("Luke Carter foi derrotado na batalha de cartas e sua alma permanecera na cabana para todo o sempre!")
    condicao = False
  
  round += 1
