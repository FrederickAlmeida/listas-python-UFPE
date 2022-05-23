# fatorial de um número

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# a recursão é um caso especial de iteração, por exemplo:
#
# while condicao:
#   do(something)
#
# def func_rec():
#   if condicao:
#       do(something)
#       func_rec()

def printar_n(x):
    if x > 0:
        print(x)
        printar_n(x-1)

def produto(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 0
    else:
        return a + produto(a, b-1)

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

x = []
for numero in range(14):
    x.append(fibonacci(numero))

for element in x:
    if element == x[-1]:
        print(element)
    else:
        print(element, end=", ")