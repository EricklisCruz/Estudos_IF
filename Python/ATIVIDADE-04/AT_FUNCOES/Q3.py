lista = []
#função com parâmetro definido
def listaElementos(num=10):
    num 
    return num 
#função para adicionar os valores a lista e fazer 
#a soma da quantidade de números pares
def pares():
    for i in range(0,listaElementos()):
        nume = int(input('Digite um número: '))
        lista.append(nume)

    c = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            c = c + 1

    print(f'A quantidade de núremos pares é {c}')

pares()



