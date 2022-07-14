#Criação de diciónario para leitura da chave solicitada referente ao seu mês
dic = {1:'janeiro', 2:'Fevereiro', 3:'Março', 4:'April', 5:'Maio',
        6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro',
        11:'Novembro', 12:'Dezembro'}

#Função para leitura do valor referente a chave solicitada pelo usúario
def chaveMes(num):   
    a = dic[num]      
    return a
    

#Função principal
def main():
    nume = int(input('Digite um número de 1 a 12 para saber o mêsde referência: '))
    #Condição para casa o usúario digite um número inválido
    b = chaveMes(nume)
    print(f'O mês referente ao número {nume} é o mês de {b}')
main()