nomes = []
nome = 0

print('Para finalizar digite uma string vazia!')

while nome != 1:
    if nome != '':
        nome = str(input('Digite um nome: '))
        if nome == '':
            break
        else:
            nomes.append(nome)    
    else:
        break

for i in range(0,1):
    print(nomes)