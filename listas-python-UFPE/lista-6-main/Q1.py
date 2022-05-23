def func_mdc(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return func_mdc(a%b, b)
    elif a < b:
        return func_mdc(a, b%a)
    elif a == b:
        return a

pokebolas = int(input())
pocoes = int(input())
revives = int(input())

mdc = func_mdc(pokebolas, pocoes)
mdc = func_mdc(mdc, revives)

if mdc > 1:
    print(f"Gracas a Companhia Pokemon, {mdc} treinadores pokemon vao receber itens do Professor!")
elif mdc == 1:
    print(f"Infelizmente apenas 1 treinador pokemon ira receber os itens hoje, e com certeza nao e o atrasado do Ash.")