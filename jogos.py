
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
    
    return estoque
    