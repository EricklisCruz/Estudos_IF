lista = [2,4,10,6,1,5,7]
par = lambda n: n%2 == 0
impar = lambda n: n%2 != 0
par1 = filter(par,lista)
impar1=filter(impar,lista)
paress = list(map(lambda n: n*2,par1))
imparrr=list(map(lambda n: n - 1,impar1))
g = paress+imparrr
print(g)
