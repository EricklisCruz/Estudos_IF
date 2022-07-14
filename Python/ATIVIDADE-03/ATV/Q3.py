lista = []
dic = {}

for i in range(0,5):
    dic['nome'] = str(input('Digite seu nome: ')) 
    dic['email'] = str(input('Digite seu email: '))
    
    lista.append(dic.copy())

for i in range(0,1):
    print(lista)
