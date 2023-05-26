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
      
    #Verificando os testes que falharam e passaram 
    
    if(-1 not in estoque):
        testesCertos += 1
    
    if (testesCertos == 3):
        print("Teste passou com sucesso!\n")
    
    else:
        print("Teste falhou\n")

#Testando a função de ordenar estoque

def testeBuscaJogo():
    testesCertos = 0
    #Estoque de exemplo
    
    estoque = []
    jogos = ["Xadrez","Jogo da vida","Monopoly","Detetive","Baralho"]
    precos = [20.00,45.50,56.79,48.99,3.99]
    qtds = [8,20,50,35,90]
    
    for i in range(len(jogos)):
        incluiJogo(estoque,jogos[i],precos[i],qtds[i])
        
    #Testes em que o jogo é encontrado
    
    #Buscar por detetive
    
    if(testaResultados(estoque[1],buscaJogo("Detetive",estoque))):
       testesCertos += 1
    
    #Buscar por xadrez
    
    if(testaResultados(estoque[4],buscaJogo("Xadrez",estoque))):
       testesCertos += 1
    
    #Teste que o jogo não é encontrado
    
    if(testaResultados(-1,buscaJogo("Jogo da velha",estoque))):
       testesCertos += 1
       
    #Verificando os testes que falharam e passaram
    
    if(testesCertos == 3):
        print("Teste passou com sucesso!\n")
    
    else:
        print("Teste falhou\n")

#Testando a função de acrescentar jogos

def testeAcrescentaJogo():
    #Estoque de exemplo
    testesCertos = 0
    
    estoque = []
    jogos = ["Xadrez","Jogo da vida","Monopoly","Detetive","Baralho"]
    precos = [20.00,45.50,56.79,48.99,3.99]
    qtds = [8,20,50,35,90]
    
    for i in range(len(jogos)):
        incluiJogo(estoque,jogos[i],precos[i],qtds[i])
    
    #teste que acrescenta a quantidade do jogo xadrez
    
    acrescentaJogo("Xadrez",estoque)
    
    if(testaResultados(18,estoque[4]["qtd"])):
        testesCertos += 1
    
    #teste que não acrescenta a quantidade do jogo que não existe
    
    acrescentaJogo("Jogo da velha",estoque)
    
    if(testaResultados(-1,acrescentaJogo("Jogo da velha",estoque))):    
        testesCertos += 1
        
    #Verificando os testes que falharam e passaram
    
    if(testesCertos == 2):
        print("Teste passou com sucesso!\n")
        
    else:
        print("Teste falhou\n")

#Testando função de receber preferência de jogo

def testeRecebePreferencia():
    testesCertos = 0
    
    #Estoque de exemplo
    
    estoque = []
    jogos = ["Xadrez","Jogo da vida","Monopoly","Detetive","Baralho"]
    precos = [20.00,45.50,56.79,48.99,3.99]
    qtds = [8,20,50,35,90]
    
    for i in range(len(jogos)):
        incluiJogo(estoque,jogos[i],precos[i],qtds[i])
        
    #Teste que retorna o jogo preferido com a quantidade certa
    
    if(testaResultados("Damas",preferenciaJogo("Damas",29.90,estoque))):
        if(testaResultados(10,estoque[1]["qtd"])):
            testesCertos += 1
    
    #Teste que acrescenta um jogo já existente
    
    if(testaResultados("Xadrez",preferenciaJogo("Xadrez",20.00,estoque))):
        if(testaResultados(18,estoque[5]["qtd"])):
            testesCertos += 1
            
    #Teste que há erros na inserção
    
    if(testaResultados(-1,preferenciaJogo("Jogo da velha","20.00",estoque))):
        testesCertos += 1
        
    
    #Verificando os testes que falharam e passaram
    
    if(testesCertos == 3):
        print("Teste passou com sucesso!\n")
        
    else:
        print("Teste falhou\n")
    
#Testando a função de excluir jogos

def testeExcluiJogo():
    
    testesCertos=0
    
    #Estoque de exemplo
    
    estoque = []
    
    jogos = ["Xadrez","Jogo da vida","Monopoly","Detetive","Baralho"]
    precos = [20.00,45.50,56.79,48.99,3.99]
    qtds = [8,20,50,35,90]
    
    for i in range(len(jogos)):
        incluiJogo(estoque,jogos[i],precos[i],qtds[i])
        
    #Teste que exclui o jogo monopoly
    
    excluiJogo("Monopoly",estoque)
    
    if(testaResultados(-1,buscaJogo("Monopoly",estoque))):
        testesCertos += 1
    
    #Teste que não exclui o jogo que não existe
    
    excluiJogo("Jogo da velha",estoque) 
    
    if(testaResultados(-1,excluiJogo("Jogo da velha",estoque))):
        testesCertos += 1
    
    #Verificando os testes que falharam e passaram
    
    if(testesCertos == 2):
        print("Teste passou com sucesso!\n")
        
    else:
        print("Teste falhou\n")
        
 
 #Testando a função de altear dados de um jogo

#Testando a função de alterar dados de um jogo

def testeAlteraJogo():
     
    testesCertos = 0
     
    #Estoque de exemplo
    
    estoque = []
    
    jogos = ["Xadrez","Jogo da vida","Monopoly","Detetive","Baralho"]
    precos = [20.00,45.50,56.79,48.99,3.99]
    qtds = [8,20,50,35,90]
    
    for i in range(len(jogos)):
        incluiJogo(estoque,jogos[i],precos[i],qtds[i])
    
    #Teste que altera o preço do jogo monopoly
    
    alteraJogo("Monopoly","Monopoly",69.99,50,estoque)
    
    if(testaResultados(69.99,estoque[3]['preco'])):
        testesCertos += 1
   
    #Teste que não altera o preço do jogo que não existe
    
    if(testaResultados(-1,alteraJogo("Jogo da velha","Jogo da Velha",20.00,10,estoque))):
        testesCertos += 1
    
    #Teste que altera a quantidade do jogo detetive
    
    alteraJogo("Detetive","Detetive",48.99,40,estoque)
    
    if(testaResultados(40,estoque[1]['qtd'])):
        testesCertos += 1
    
    #Teste que altera o nome do jogo baralho
    
    alteraJogo("Baralho","Cartas",3.99,90,estoque)
    
    if(testaResultados(estoque[0],buscaJogo("Cartas",estoque))):
        testesCertos += 1
        
    #Teste que altera o nome do jogo Detetive
    
    alteraJogo("Detetive","Mistério",48.99,35,estoque)
    
    if(testaResultados(estoque[2],buscaJogo("Mistério",estoque))):
        testesCertos += 1
    
    #Verificando os testes que falharam e passaram
    
    if(testesCertos == 5):
        print("Teste passou com sucesso!\n")
        
    else:
        print("Teste falhou\n")

#Testando a função de exibir jogos no estoque

def testeExibeJogos():
    testesCertos = 0
    #Estoque de exemplo que dá certo
    
    estoque = []
    
    jogos = ["Xadrez","Jogo da vida","Monopoly","Detetive","Baralho"]
    precos = [20.00,45.50,56.79,48.99,3.99]
    qtds = [8,20,50,35,90]
    
    for i in range(len(jogos)):
        incluiJogo(estoque,jogos[i],precos[i],qtds[i])
    
    if(testaResultados(1,exibeEstoque(estoque))):
        testesCertos += 1
    
    #Estoque de exemplo que dá errado
    
    estoque = []
    
    if(testaResultados(-1,exibeEstoque(estoque))):
        testesCertos += 1
    
    #Verificando os testes que falharam e passaram
    
    if(testesCertos == 2):
        print("Teste passou com sucesso!\n")
        
    else:
        print("Teste falhou\n")


#Testando a função de venda de jogos

def testeVendaJogo():
    
    testesCertos = 0
    
    #Estoque de exemplo
    
    estoque = []
    
    jogos = ["Xadrez","Jogo da vida","Monopoly","Detetive","Baralho"]
    precos = [20.00,45.50,56.79,48.99,3.99]
    qtds = [8,20,50,35,90]
    
    for i in range(len(jogos)):
        incluiJogo(estoque,jogos[i],precos[i],qtds[i])
        
    #Teste que vende 1 jogo monopoly
    
    vendeJogo("Monopoly",estoque,56.79,1)
    
    if(testaResultados(49,estoque[3]['qtd'])):
        testesCertos += 1
    
    #Teste que tenta comprar 9 jogos de xadrez e não consegue
    
    if(testaResultados(-1,vendeJogo("Xadrez",estoque,180.00,9))):
        testesCertos += 1
        
    #Teste que tenamos comprar 2 jogos de baralho e nao tem dinheiro suficiente
    
    if(testaResultados(-1,vendeJogo("Baralho",estoque,3.50,2))):
        testesCertos += 1
        
    #Teste que tenta comprar um jogo que não existe
    
    if(testaResultados(-1,vendeJogo("Jogo da velha",estoque,20.00,1))):
        testesCertos += 1
    
    #Verificando os testes que falharam e passaram
    
    if(testesCertos == 4):
        print("Teste passou com sucesso!\n")
    
    else:
        print("Teste falhou\n")
    
    
print("Testando função monta jogos:\n")
testeMontaJogos()

print("Testando função inclui jogos:\n")
testeIncluiJogos()

print("Testando função busca jogos:\n")
testeBuscaJogo()

print("Testando função acrescenta jogos:\n")
testeAcrescentaJogo()

print("Testando função recebe preferencia:\n")
testeRecebePreferencia()

print("Testando função exclui jogos:\n")
testeExcluiJogo()

print("Testando função altera jogos:\n")
testeAlteraJogo()

print("Testando função exibe jogos:\n")
testeExibeJogos()

print("Testando função vende jogos:\n")
testeVendaJogo()