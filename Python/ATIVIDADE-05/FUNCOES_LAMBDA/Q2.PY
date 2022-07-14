lista = []
for i in range(0,10):
    num = int(input('Digite um número:'))
    lista.append(num)
pares = lambda par : par % 2 == 0
a = list(filter(pares,lista))
print('Os números pares são:',a)
