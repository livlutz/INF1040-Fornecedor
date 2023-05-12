from jogos import *

#função auxiliar de teste que compara 2 valores, retornando o resultado da comparação
def testaResultados(esperado,recebido):
    return esperado == recebido

#Testando a função de montar jogos

def testeMontaJogos():
    #Variável de contagem de testes que dão certo
    
    testesCertos = 0
    
    #Teste que dá certo,retorna um jogo montado
    jogo1 = montaJogo("jogo da velha",10.00,90)
    
    certo = {
        'nome' : "jogo da velha",
        'preco': 10.00,
        'qtd' : 90
    }
    
    if(testaResultados(certo,jogo1) == 1):
        testesCertos += 1
        
    #Teste que dá errado, montando um jogo com dados inválidos e retornando -1
    
    jogo2 = montaJogo(2,"5.9",80)
    
    if(testaResultados(-1,jogo2) == 1):
        testesCertos += 1
        
    #Verificando os testes que falharam e passaram
        
    if(testesCertos == 2):
        print("Teste passou com sucesso!\n")
    
    else:
        print("Teste falhou\n")

#Testando a função de incluir jogos

def testeIncluiJogos():
    testesCertos = 0
    
    #Teste que inclui jogo na lista vazia
    estoque = []
    
    incluiJogo(estoque,"Jogo da velha",10.50,8)
    
    if(-1 not in estoque):
        testesCertos += 1
    
    #Teste que não inclui o jogo no estoque por dados inválidos
    estoque2 = []
    
    incluiJogo(estoque2,"Jogo da velha","20,00",6)
    
    if(testaResultados(-1,incluiJogo(estoque2,"Jogo da velha","20,00",6))):
        testesCertos += 1
    
    #Teste de inclusão de vários jogos no estoque não vazio 
    
    jogos = ["Xadrez","Jogo da vida","Monopoly","Detetive","Baralho"]
    precos = [20.00,45.50,56.79,48.99,3.99]
    qtds = [8,20,50,35,90]
    
    for i in range(len(jogos)):
        incluiJogo(estoque,jogos[i],precos[i],qtds[i])
    
    if(-1 not in estoque):
        testesCertos += 1
    
    if (testesCertos == 3):
        print("Teste passou com sucesso!\n")
    
    else:
        print("Teste falhou\n")
        

print("Testando função monta jogos:\n")
testeMontaJogos()

print("Testando função inclui jogos:\n")
testeIncluiJogos()