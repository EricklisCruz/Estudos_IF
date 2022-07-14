positivo = lambda n: n > 0

lista = [1,2,3,-4,5,-6]

retiraNegativo = list(filter(positivo,lista))

print('Lista com os números inteiros negativos e positivos:', lista)
print('A lista apenas com os números positivos: ',retiraNegativo)