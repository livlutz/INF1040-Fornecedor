
#Monta um novo jogo (dicionário) a partir do seu nome (string), preço (float) e quantidade (int)

def montaJogo(nome,preco,quantidade):
    
    if(type(nome) == str and type(preco) == float and type(quantidade) == int):
        jogo = {
            'nome' : nome,
            'preco' : preco,
            'qtd' : quantidade
        }
        
        return jogo
    
    else:
        return -1
    
#Monta um jogo e o inclui no estoque na última posição

def incluiJogo(estoque,nome,preco,quantidade):
    jogo = montaJogo(nome,preco,quantidade)
    
    if(jogo == -1):
        return -1
    
    estoque.append(jogo)
    
    estoque = ordenaEstoque(estoque)
    
    return estoque

#Função auxiliar na ordenação que pega o nome de um jogo no estoque

def getNome(estoque):
    return estoque['nome']

#Função auxiliar na inclusão que ordena os jogos no estoque por ordem alfabética

def ordenaEstoque(estoque):
    if isinstance(estoque, list):
        estoque.sort(key = getNome)
        return estoque
    
    else:
        return -1

#Função auxiliar para busca que compara 2 strings de nome

def comparaNomes(nome1,nome2):
    
    if(nome1 > nome2):
        return 1
    
    elif (nome1 < nome2):
        return -1
    
    else:
        return 0
    
#Função de buscar jogos por nome no estoque
    
def buscaJogo(nome, estoque):
    inicio = 0
    fim = len(estoque) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        jogo = estoque[meio]

        comp = comparaNomes(nome, jogo['nome'])

        if (comp < 0):
            fim = meio - 1
            
        elif (comp > 0):
            inicio = meio + 1
            
        else:
            return jogo

    print("Jogo não encontrado\n")
    return -1

#Função que acrescenta um jogo no estoque

def acrescentaJogo(nome,estoque):
    jogo = buscaJogo(nome,estoque)

    if(jogo == -1):
        return -1
    
    jogo['qtd'] += 10
    
    return estoque

#Função que recebe a preferência de um jogo,inclui e acrescenta o jogo no estoque

def preferenciaJogo(nome,preco,estoque):
    
    if(buscaJogo(nome,estoque) == -1):
        estoque = incluiJogo(estoque,nome,preco,0)
        
        if(estoque == -1):
            return -1
        
        estoque = acrescentaJogo(nome,estoque)
        
        return nome
    
    else:
        estoque = acrescentaJogo(nome,estoque)
        
        if(estoque == -1):
            return -1
        
        return nome
        
        