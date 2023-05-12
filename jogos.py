
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
    