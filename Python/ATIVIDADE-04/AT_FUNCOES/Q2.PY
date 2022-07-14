#Função que recebe número inteiro e executa a soma
def numSoma(num):
    soma = 0
    #Condição para caso o usuário digitar um número negativo não retornar soma
    if num < 1:
        print(f'O número {num} não é um número inteiro positivo!')
    else:
        for i in range(1,num+1):
            soma = soma + i
            
        return soma

#Função principal do programa
def main():
    nume = int(input('Digite um número inteiro positivo: '))
    a = numSoma(nume)
    print(f'A soma dos números até {nume} é igual a: {a}')
    
#Invocar função
main()