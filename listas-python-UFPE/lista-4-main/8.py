# {NOME_1}, {QTD_SEGUIDORES_1}, {QTD_VIEWS_1}, {CATEGORIA_1}
# restrições: max
qtd_tiktokers = int(input())
tiktokers_lifestyle = []
tiktokers_dancinhas = []
tiktokers_utilidades = []

for tiktoker in range(qtd_tiktokers):
  auxiliar = input().split(", ")
  if auxiliar[1][-1] == "M":  # eliminar o M e o K dos seguidores, para poder calcular a média posteriormente (não esqueça de botar dnv no final, qnd for printar)
    auxiliar[1] = float(auxiliar[1][0:-1])*1000
  elif auxiliar[1][-1] == "K":
    auxiliar[1] = float(auxiliar[1][0:-1])
  if auxiliar[2][-1] == "M":
    auxiliar[2] = float(auxiliar[2][0:-1])*1000
  elif auxiliar[2][-1] == "K":
    auxiliar[2] = float(auxiliar[2][0:-1])
  if auxiliar[3] == "Dancinhas":
    tiktokers_dancinhas.append(auxiliar)
  elif auxiliar[3] == "Lifestyle":
    tiktokers_lifestyle.append(auxiliar)
  elif auxiliar[3] == "Utilidades":
    tiktokers_utilidades.append(auxiliar)

# média de seguidores
if len(tiktokers_lifestyle) > 0:      
  auxiliar2 = 0.0
  for element in tiktokers_lifestyle:
    auxiliar2 += element[1]
  media_lifestyle = auxiliar2/(1000*len(tiktokers_lifestyle))

if len(tiktokers_utilidades) > 0:
  auxiliar2 = 0.0
  for element in tiktokers_utilidades:
    auxiliar2 += element[1]
  media_utilidades = auxiliar2/(1000*len(tiktokers_utilidades))

if len(tiktokers_dancinhas) > 0:
  auxiliar2 = 0.0
  for element in tiktokers_dancinhas:
    auxiliar2 += element[1]
  media_dancinhas = auxiliar2/(1000*len(tiktokers_dancinhas))

# maximo de visualizações
if len(tiktokers_lifestyle) > 0:
  auxiliar3 = 0.0
  for element in tiktokers_lifestyle:
    if element[2] > auxiliar3:
      auxiliar3 = element[2]
  maximo_lifestyle = auxiliar3/1000

if len(tiktokers_utilidades) > 0:
  auxiliar3 = 0.0
  for element in tiktokers_utilidades:
    if element[2] > auxiliar3:
      auxiliar3 = element[2]
  maximo_utilidades = auxiliar3/1000

if len(tiktokers_dancinhas) > 0:
  auxiliar3 = 0.0
  for element in tiktokers_dancinhas:
    if element[2] > auxiliar3:
      auxiliar3 = element[2]
  maximo_dancinhas = auxiliar3/1000

# printar os resultados
print("Lifestyle;")
if len(tiktokers_lifestyle) > 0:
  print(f"Quantidade de Tiktokers: {len(tiktokers_lifestyle)}")
  print(f"Media de seguidores: {int(media_lifestyle*10)/10}M")
  print(f"Maximo de visualizações: {maximo_lifestyle:.2f}M\n")
else:
  print("Nao foram informados dados sobre esta categoria.\n")

print("Utilidades;")
if len(tiktokers_utilidades) > 0:
  print(f"Quantidade de Tiktokers: {len(tiktokers_utilidades)}")
  print(f"Media de seguidores: {int(media_utilidades*10)/10}M")
  print(f"Maximo de visualizações: {maximo_utilidades:.2f}M\n")
else:
  print("Nao foram informados dados sobre esta categoria.\n")

print("Dancinhas;")
if len(tiktokers_dancinhas) > 0:
  print(f"Quantidade de Tiktokers: {len(tiktokers_dancinhas)}")
  print(f"Media de seguidores: {int(media_dancinhas*10)/10}M")
  print(f"Maximo de visualizações: {maximo_dancinhas:.2f}M\n")
else:
  print("Nao foram informados dados sobre esta categoria.\n")

# tiktoker com mais seguidores
mais_famoso = []
lista_auxiliar = []

if len(tiktokers_dancinhas) > 0:
  for element in tiktokers_dancinhas:
    lista_auxiliar.append(element)

if len(tiktokers_lifestyle) > 0:
  for element in tiktokers_lifestyle:
    lista_auxiliar.append(element)

if len(tiktokers_utilidades) > 0:
  for element in tiktokers_utilidades:
    lista_auxiliar.append(element)

auxiliar4 = 0
for element in lista_auxiliar:
  if element[1] > auxiliar4:
    auxiliar4 = element[1]  
    mais_famoso.append(element)  # assim, o ultimo elemento será o com mais seguidores
  
print(f"Os olhares do mundo estao sobre {mais_famoso[-1][0].upper()}, que conta com {mais_famoso[-1][1]/1000:.1f}M de seguidores vendo seus videos diarios de {mais_famoso[-1][3]}!")