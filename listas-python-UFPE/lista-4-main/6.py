condicao = True
comecar = input()
lista_ordenada = []

while condicao:
  if comecar == "editar":
    acao = input()
    convidado = input()
    while acao != "lista finalizada:":
      acao = input()
      if acao == "adicionar":
        lista_ordenada.insert(int(convidado.split(" ")[1]), convidado.split(" ")[0])
      elif acao == "remover":
        lista_ordenada.remove(convidado.split(" ")[0])
      elif acao == "atualizar indice":  # realmente precisa fazer o processo 2x?
        if lista_ordenada.index(convidado.split(" ")[0]) == convidado.split(" ")[1]:
          print("Nada mudou, a lista permanece igual")
        else:
          lista_ordenada.remove(convidado.split(" ")[0])
          lista_ordenada.insert(int(convidado.split(" ")[1]), convidado.split(" ")[0])
      elif acao == "imprimir lista atual":
        for element in lista_ordenada:
          if element != (len(lista_ordenada)-1):
            print(element, end=" ")
          else:
            print(element)
      elif acao == "lista finalizada":
        condicao = False
      else:
        print("Opçao não encontrada")
  else:
    continue

print("A lista ficou da seguinte forma:")
for element in lista_ordenada:
  if element != (len(lista_ordenada)-1):
    print(element, end=" ")
  else:
    print(element)