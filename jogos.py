#Estrutura de dados para armazenar os jogos

jogo = {
    "nome" : None, #nome do jogo
    "preco": None, #preço do jogo
    "qtd": None #quantidade do jogo no estoque
}

#Monta um novo jogo (dicionário) a partir do seu nome (string), preço (float) e quantidade (int)

def montaJogo(nome,preco,quantidade):
    #Verifica se os dados são válidos
    
    if(isinstance(nome,str) and isinstance(preco,float) and isinstance(quantidade,int)):
        #Cria um novo jogo com base no dicinário jogo e atribui os valores passados como parâmetro
        novo_jogo = jogo.copy()
        
        novo_jogo["nome"] = nome
        
        novo_jogo["preco"] = preco
        
        novo_jogo["qtd"] = quantidade
        
        #Exibe mensagem de sucesso caso o jogo seja montado corretamente
        
        print("Jogo montado com sucesso\n")
        
        #Retorna o novo jogo
        
        return novo_jogo
    
    #Exibe mensagem de erro caso os dados sejam inválidos ou o jogo não seja montado corretamente
    else:
        print("Erro: dados inválidos\n")
        
        #Retorna -1 para indicar que o jogo não foi montado corretamente
        return -1
    
#Monta um jogo e o inclui no estoque na última posição

def incluiJogo(estoque,nome,preco,quantidade):
    #Verifica se os dados são válidos montando o jogo
    novo_jogo = montaJogo(nome, preco, quantidade)
    
    #Verifica se o jogo foi montado corretamente, exibindo mensagem de erro caso contrário
    if(novo_jogo == -1):
        print("Erro: dados inválidos, não foi possível incluir o jogo\n")   
        return -1
    
    #inclui o jogo no estoque
    estoque.append(novo_jogo)
    
    #Ordena o estoque por nome, usando a função auxiliar getNome
    estoque.sort(key = getNome)
    
    #Exibe mensagem de sucesso caso o jogo seja incluído corretamente
    
    print("Jogo incluído com sucesso\n")
    
    #Retorna o estoque atualizado com o novo jogo
    
    return estoque

#Função auxiliar na ordenação que pega o nome do jogo no estoque

def getNome(jogo):
    return jogo["nome"]

#Função auxiliar para busca que compara 2 strings de nome

def comparaNomes(nome1,nome2):
    
    #Verifica se os nomes são strings
    if(not isinstance(nome1,str) or not isinstance(nome2,str)):
        print("Erro: nome inválido\n")
    
    #Compara os valores ASCII dos primeiros caracteres de cada string
    
    #Retorna 1 se o primeiro nome for maior (estiver depois em ordem alfabética) que o segundo
    if(nome1 > nome2):
        return 1
    
    #Retorna -1 se o primeiro nome for menor (estiver antes em ordem alfabética) que o segundo
    
    elif (nome1 < nome2):
        return -1
    
    #Retorna 0 se os nomes forem iguais
    
    else:
        return 0
    
#Função de buscar jogos por nome no estoque
    
def buscaJogo(nome,estoque):
    #Iniciando a busca no estoque com o primeiro e último índice
    inicio = 0
    fim = (len(estoque) - 1)
    
    #Enquanto o índice inicial for menor ou igual ao final, percorremos o estoque
    
    while(inicio <= fim):
        
        #Calculamos o índice do meio do estoque
        
        meio = (inicio + fim) // 2
        
        #Pegamos o jogo do meio do estoque
        
        j = estoque[meio]
        
        #Comparamos os nomes dos jogos procurado e do meio do estoque
        
        resultado = comparaNomes(nome,getNome(j))
        
        #Se o resultado for diferente de None, significa que os nomes são strings e podemos compará-los
        
        if(resultado != None):
            
            #Se o resultado for menor que 0, significa que o nome procurado está antes do nome do meio do estoque
            if(resultado < 0):
                fim = meio - 1
            
            #Se o resultado for maior que 0, significa que o nome procurado está depois do nome do meio do estoque
            elif(resultado > 0):
                inicio = meio + 1
            
            #Se o resultado for igual a 0, significa que o nome procurado é igual ao nome do meio do estoque
            else:
                #Exibe mensagem de sucesso e retorna o jogo encontrado
                print("Jogo encontrado\n")
                return j
        
        #Se o resultado for None, significa que os nomes não são strings e não podemos compará-los
        else:
            break
    
    #Exibe mensagem de erro e retorna -1 caso o jogo não seja encontrado ou os nomes não sejam strings (Dados inválidos)
    print("Jogo não encontrado\n")
    return -1

#Função que acrescenta um jogo no estoque

def acrescentaJogo(nome,estoque):
    #Busca o jogo no estoque
    jogo = buscaJogo(nome,estoque)
    
    #Verifica se o jogo foi encontrado, exibindo mensagem de erro e retornando -1 caso contrário

    if(jogo == -1):
        return -1
    
    #Se o jogo foi encontrado, acrescenta 10 unidades no estoque
    
    jogo["qtd"] += 10
    
    #Exibe mensagem de sucesso
    
    print("Estoque abastecido com sucesso\n")
    
    #Retorna o estoque atualizado
    
    return estoque

#Função que recebe a preferência de um jogo,inclui e acrescenta o jogo no estoque

def preferenciaJogo(nome,preco,estoque):
    
    #Verifica se o jogo já está no estoque
    
    #Se não estiver, inclui o jogo no estoque e acrescenta 10 unidades
    if(buscaJogo(nome,estoque) == -1):
        estoque = incluiJogo(estoque,nome,preco,0)
        
        #Verifica se o jogo foi incluído corretamente, exibindo mensagem de erro e retornando caso contrário
        if(estoque == -1):
            return -1
        
        #Se o jogo foi incluído corretamente, acrescenta 10 unidades no estoque
        
        estoque = acrescentaJogo(nome,estoque)
        
        #Exibe mensagem de sucesso caso o jogo seja incluído e acrescentado corretamente
        
        print("Preferência feita\n")
        
        #Retorna o nome do jogo adicionado
        
        return nome
    
    else:
        
        #Se o jogo já estiver no estoque, apenas acrescenta 10 unidades
        estoque = acrescentaJogo(nome,estoque)
        
        #Verifica se o jogo foi acrescentado corretamente, exibindo mensagem de erro e retornando caso contrário
        
        if(estoque == -1):
            return -1
        
        #Exibe mensagem de sucesso caso o jogo já existente seja acrescentado corretamente
        print("Preferência já existente. Estoque abastecido em 10 unidades\n")
        
        #Retorna o nome do jogo adicionado
        
        return nome
        
#Função de excluir jogo do estoque

def excluiJogo(nome,estoque):
    
    #Busca o jogo no estoque
    jogo = buscaJogo(nome,estoque)
    
    #Verifica se o jogo foi encontrado, exibindo mensagem de erro e retornando -1 caso contrário
    
    if(jogo == -1):
        return -1
    
    #Se o jogo foi encontrado, exclui o jogo do estoque
    
    estoque.remove(jogo)
    
    #Exibe mensagem de sucesso
    
    print("Jogo excluído com sucesso\n")
    
    #Retorna o nome do jogo excluído
    
    return nome       

#Função de alterar dados de um jogo

def alteraJogo(nomeJogo,nomeNovo,preco,quantidade,estoque):
    
    #Busca o jogo no estoque
    jogo = buscaJogo(nomeJogo,estoque)
    
    #Verifica se o jogo foi encontrado, exibindo mensagem de erro e retornando -1 caso contrário
    if(jogo == -1):
        return -1
    
    #Verifica se os dados são válidos, exibindo mensagem de erro e retornando -1 caso contrário
    
    if(isinstance(preco,float) == False or isinstance(quantidade,int) == False or isinstance(nomeNovo,str) == False):
        print("Erro: dados inválidos\n")
        return -1
    
    #Altera os dados do jogo
    
    jogo["preco"] = preco
    jogo["qtd"] = quantidade
    jogo["nome"] = nomeNovo
    
    #Ordena o estoque por nome usando a função auxiliar getNome como chave
    
    estoque.sort(key = getNome)
    
    #Exibe mensagem de sucesso
    
    print("Jogo alterado com sucesso\n")
    
    #Retorna 1 caso o jogo seja alterado corretamente
    
    return 1

#Função que exibe todos os jogos no estoque

def exibeEstoque(estoque):
    
    #Verifica se o estoque está vazio, exibindo mensagem de erro e retornando -1 caso esteja vazio
    if(len(estoque) == 0):
        print("Estoque vazio\n")
        return -1
    
    #Exibe todos os dados de todos os jogos no estoque
    for jogo in estoque:
        print('Nome: %s '  %(getNome(jogo)))
        print('Preço: %s ' %(str(jogo["preco"])))
        print('Quantidade: %s ' % (str(jogo["qtd"])))
        print('-----------------------')
        
    #Retorna 1 caso o estoque seja exibido corretamente
    
    return 1

#Função de solicitar compra de um jogo

def solicitaCompra(nome,estoque,valorPagar,qtdCompra):
    
    #Busca o jogo no estoque
    j = buscaJogo(nome,estoque)
    
    #Verifica se o jogo foi encontrado, exibindo mensagem de erro e retornando -1 caso contrário
    
    if(j == -1):
        print("Jogo não encontrado")
        return -1
    
    #Verfica se a quantidade de determinado jogo é suficiente para a compra, exibindo mensagem de erro e retornando -1 caso contrário
    
    elif(qtdCompra > j["qtd"]):
        print("Quantidade insuficiente no estoque")
        return -1
    
    #Verifica se o valor a ser pago é suficiente para a compra, exibindo mensagem de erro e retornando -1 caso contrário
    
    elif(valorPagar < j["preco"]):
        print("Valor insuficiente")
        return -1
    
    #Caso as condições sejam satisfeitas, exibe mensagem de sucesso e retorna 1
    else:
        print("Compra autorizada")
        return 1

#Função de vender um jogo

def vendeJogo(nome,estoque,valorPagar,qtdCompra):
    
    #Verifica se a compra é autorizada, exibindo mensagem de erro e retornando -1 caso contrário
    
    if(solicitaCompra(nome,estoque,valorPagar,qtdCompra) == -1):
        print("Erro: não foi possível realizar a compra\n")
        return -1
    
    #Busca o jogo no estoque
    
    j = buscaJogo(nome,estoque)
    
    #Decrementa a quantidade de jogos no estoque de acordo com a quantidade comprada
    
    for i in range(qtdCompra):  
        j["qtd"] -= 1
    
    
    #Exibe mensagem de sucesso
    
    print("Compra realizada com sucesso\n")
    
    #Retorna 1 caso a compra seja realizada corretamente
    
    return 1
