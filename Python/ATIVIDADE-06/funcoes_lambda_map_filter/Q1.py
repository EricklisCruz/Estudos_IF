lista = []

for i in range(0,5):
    w = int(input('Digite um número:'))
    lista.append(w)
y = int(input('Digite o número que você deseja saber quantas vezes ele foi digitado: '))
vezes = lambda n: n == y

repetiu = list(filter(vezes,lista))
print(lista)
if len(repetiu) <=1:
    print(f'O número {y} repetiu',len(repetiu), 'vez')
else:
    print(f'O número {y} repetiu',len(repetiu), 'vezes')
    