# fazer 2 funções: uma para calcular quantos espaços sobrando temos no inventário e outra para calcular a quantidade de slots, após conseguir x pochetes.
slots_totais = int(input())
slots_ocupados = int(input())
itens = []

def espacos_sobrando():
    return slots_totais - slots_ocupados

def quantidade_slots():
    return slots_totais + 2*pochetes_adquiridas

for item in range(slots_ocupados):
    itens.append(input().split(" - "))

pochetes_adquiridas = int(input())

print(f"Voce possui {slots_totais} slots no inventario e {slots_ocupados} estao ocupados.\nEspacos sobrando [{espacos_sobrando()}]\n")

if len(itens) == 0:
    print("Seu inventário ainda está vazio. Que sorte... ou azar. Tome cuidado.")
else:
    print("Lista de itens:")
    for item in itens:
        print(f"{item[0]} [{item[1]}]")
print("")

if pochetes_adquiridas > 0:
    print(f"Voce conseguiu {pochetes_adquiridas} pochete(s) e agora possui {quantidade_slots()} slots de inventario.\nEspacos sobrando [{quantidade_slots() - slots_ocupados}]")
else:
    print("Você ainda não encontrou pochetes. Seus espaços continuam os mesmos.")