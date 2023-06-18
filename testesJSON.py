#importando dados do arquivo JSON

import json
from jogos import *

with open('derulo.json','r') as derulo:
    data = json.load(derulo)

#data['estoque'] é o dicionario que contem os jogos

#criando um menu para o usuario

print("Bem vindo ao menu de jogos\n")
print("Digite 1 para exibir o estoque\n")
print("Digite 2 para buscar um jogo\n")
print("Digite 3 para incluir um jogo no estoque\n")
print("Digite 4 para excluir um jogo do estoque\n")
print("Digite 5 para alterar dados de um jogo\n")
print("Digite 6 para solicitar a compra de um jogo\n")
print("Digite 7 para sair\n")

opcao = int(input("Digite a opção desejada: "))

#Enquanto o usuario nao digitar 7, o menu continuará aparecendo

while(opcao != 7):
    #se o usuario digitar 1, o estoque será exibido
    if(opcao == 1):
        exibeEstoque(data['estoque'])
        
    #se o usuario digitar 2, o jogo será buscado
    
    elif(opcao == 2):
        nome = input("Digite o nome do jogo: ")
        buscaJogo(nome,data['estoque'])
        
    #se o usuario digitar 3, o jogo será incluido no estoque
    
    elif(opcao == 3):
        print("Digite os dados do jogo a ser incluido\n")
        nome = input("Digite o nome do jogo: ")
        preco = float(input("Digite o preço do jogo: "))
        quantidade = int(input("Digite a quantidade do jogo: "))
        incluiJogo(data['estoque'],nome,preco,quantidade)
    
    #se o usuario digitar 4, o jogo será excluido do estoque
    
    elif(opcao == 4):
        print("Digite os dados do jogo a ser excluido\n")
        nome = input("Digite o nome do jogo: ")
        excluiJogo(nome,data['estoque'])
    
    #se o usuario digitar 5, o jogo será alterado
    
    elif(opcao == 5):
        print("Digite os dados do jogo a ser alterado\n")
        nome = input("Digite o nome do jogo: ")
        nomeNovo = input("Digite o novo nome do jogo: ")
        preco = float(input("Digite o preço do jogo: "))
        quantidade = int(input("Digite a quantidade do jogo: "))
        alteraJogo(nome,nomeNovo,preco,quantidade,data['estoque'])
    
    #se o usuario digitar 6, o jogo será comprado
    
    elif(opcao == 6):
        print("Digite os dados do jogo a ser comprado\n")
        nome = input("Digite o nome do jogo: ")
        valorPagar = float(input("Digite o valor a ser pago: "))
        qtdCompra = int(input("Digite a quantidade a ser comprada: "))
        solicitaCompra(nome,data['estoque'],valorPagar,qtdCompra)
        
        if(solicitaCompra(nome,data['estoque'],valorPagar,qtdCompra) == 1):
           vendeJogo(nome,data['estoque'],valorPagar,qtdCompra)
        
    #se o usuario digitar 7, o programa será encerrado
    opcao = int(input("Digite a opção desejada: "))
    
#salvando dados no arquivo JSON

with open('derulo.json','w') as derulo:
    json.dump(data,derulo,indent=4)

#fechando o arquivo JSON
derulo.close()

