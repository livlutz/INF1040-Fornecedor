from jogos import *

# Criando um estoque para realizar os testes das funções
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
        
    if(testesCertos == 2):
        print("Teste passou com sucesso!\n")
    
    else:
        print("Teste falhou\n")


testeMontaJogos()