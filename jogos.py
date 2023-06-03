#Estrutura de dados para armazenar os jogos

jogo = {
    "nome" : None,
    "preco": None,
    "qtd": None
}

#Monta um novo jogo (dicionário) a partir do seu nome (string), preço (float) e quantidade (int)

def montaJogo(nome,preco,quantidade):
    if(isinstance(nome,str) and isinstance(preco,float) and isinstance(quantidade,int)):
        novo_jogo = jogo.copy()
        
        novo_jogo["nome"] = nome
        
        novo_jogo["preco"] = preco
        
        novo_jogo["qtd"] = quantidade
        
        print("Jogo montado com sucesso\n")
        
        return novo_jogo
    
    else:
        print("Erro: dados inválidos\n")
        return -1
    
#Monta um jogo e o inclui no estoque na última posição

def incluiJogo(estoque,nome,preco,quantidade):
    novo_jogo = montaJogo(nome, preco, quantidade)
    if(novo_jogo == -1):
        print("Erro: dados inválidos, não foi possível incluir o jogo\n")   
        return -1
    
    estoque.append(novo_jogo)
    estoque.sort(key = getNome)
    
    print("Jogo incluído com sucesso\n")
    
    return estoque

#Função auxiliar na ordenação que pega o nome do jogo no estoque

def getNome(jogo):
    return jogo["nome"]

#Função auxiliar para busca que compara 2 strings de nome

def comparaNomes(nome1,nome2):
    if(not isinstance(nome1,str) or not isinstance(nome2,str)):
        print("Erro: nome inválido\n")
        
    if(nome1 > nome2):
        return 1
    
    elif (nome1 < nome2):
        return -1
    
    else:
        return 0
    
#Função de buscar jogos por nome no estoque
    
def buscaJogo(nome,estoque):
    global jogo
    
    inicio = 0
    fim = len(estoque) - 1
    
    while(inicio <= fim):
        
        meio = (inicio + fim) // 2
        
        j = estoque[meio]
        
        resultado = comparaNomes(nome,getNome(j))
        
        if(resultado != None):
            if(resultado < 0):
                fim = meio - 1
            
            elif(resultado > 0):
                inicio = meio + 1
            
            else:
                print("Jogo encontrado\n")
                return j
        
        else:
            break
    
    print("Jogo não encontrado\n")
    return -1

#Função que acrescenta um jogo no estoque

def acrescentaJogo(nome,estoque):
    jogo = buscaJogo(nome,estoque)

    if(jogo == -1):
        return -1
    
    jogo["qtd"] += 10
    
    print("Estoque abastecido com sucesso\n")
    
    return estoque

#Função que recebe a preferência de um jogo,inclui e acrescenta o jogo no estoque

def preferenciaJogo(nome,preco,estoque):
    
    if(buscaJogo(nome,estoque) == -1):
        estoque = incluiJogo(estoque,nome,preco,0)
        
        if(estoque == -1):
            return -1
        
        estoque = acrescentaJogo(nome,estoque)
        
        print("Preferência feita\n")
        
        return nome
    
    else:
        estoque = acrescentaJogo(nome,estoque)
        
        if(estoque == -1):
            return -1
        
        print("Preferência já existente. Estoque abastecido em 10 unidades\n")
        
        return nome
        
#Função de excluir jogo do estoque

def excluiJogo(nome,estoque):
    jogo = buscaJogo(nome,estoque)
    
    if(jogo == -1):
        return -1
    
    estoque.remove(jogo)
    
    print("Jogo excluído com sucesso\n")
    
    return nome       

#Função de alterar dados de um jogo

def alteraJogo(nomeJogo,nomeNovo,preco,quantidade,estoque):
    jogo = buscaJogo(nomeJogo,estoque)
    
    if(jogo == -1):
        return -1
    
    if(isinstance(preco,float) == False or isinstance(quantidade,int) == False or isinstance(nomeNovo,str) == False):
        print("Erro: dados inválidos\n")
        return -1
    
    jogo["preco"] = preco
    jogo["qtd"] = quantidade
    jogo["nome"] = nomeNovo
    
    estoque.sort(key = getNome)
    
    print("Jogo alterado com sucesso\n")
    
    return 1

#Função que exibe todos os jogos no estoque

def exibeEstoque(estoque):
    if(len(estoque) == 0):
        print("Estoque vazio\n")
        return -1
    
    for jogo in estoque:
        print('Nome: %s '  %(getNome(jogo)))
        print('Preço: %s ' %(str(jogo["preco"])))
        print('Quantidade: %s ' % (str(jogo["qtd"])))
        print('-----------------------')
    
    return 1

#Função de solicitar compra de um jogo

def solicitaCompra(nome,estoque,valorPagar,qtdCompra):
    j=buscaJogo(nome,estoque)
    
    if(j == -1):
        print("Jogo não encontrado")
        return -1
    
    elif(qtdCompra > j["qtd"]):
        print("Quantidade insuficiente no estoque")
        return -1
    
    elif(valorPagar < j["preco"]):
        print("Valor insuficiente")
        return -1
    
    else:
        print("Compra autorizada")
        return 1

#Função de vender um jogo

def vendeJogo(nome,estoque,valorPagar,qtdCompra):
    
    if(solicitaCompra(nome,estoque,valorPagar,qtdCompra) == -1):
        print("Erro: não foi possível realizar a compra\n")
        return -1
    
    j = buscaJogo(nome,estoque)
    
    j["qtd"] -= qtdCompra
    
    print("Compra realizada com sucesso\n")
    
    return 1
