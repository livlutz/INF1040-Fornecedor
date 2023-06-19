#Importando dados do arquivo JSON
import json
import os.path
from jogos import *

#precoPadrao é o preço que sera acrescentado ao jogo que tiver preferencia pela locadora e que nao estiver presente no estoque
precoPadrao = 29.99

#Usaremos 3 Arquivos: de pedido/requerimento com o nome do jogo 
# de resposta com o stauts se o jogo pedido existe ou não no estoque da fornecedora
# e de preferência com o nome do jogo que terá a preferência pela locadora

#OBS: Os nomes dos jogos usados tanto pela fornecedora quanto pela locadora estão em capslock e sem acentos

#Função que le o arquivo JSON de pedido com o nome do jogo que sera buscado

def receberPedido():
    #Verificando se o arquivo existe
    file_exists = os.path.isfile('requerimentos.json')
    
    if(file_exists == False):
        print("Arquivo de requerimentos inexixtente\n")
    
    else:
        #Lendo dados do arquivo JSON de pedidos/ requerimentos com o nome do jogo 
        with open('requerimentos.json','r') as requerimentos:
            info = json.load(requerimentos)
            
            #Fechando o arquivo 
            requerimentos.close()
            
            #info tem o nome do jogo
            return info

#Função que lê o arquivo JSON de preferência com o nome do jogo que terá uma preferência pela locadora

def receberPreferencia():
    #Verificando se o arquivo existe
    file_exists = os.path.isfile('preferencia.json')
    
    if(file_exists == False):
        print("Arquivo de preferencias inexistente\n")
    
    #Lendo dados do arquivo JSON de preferências com o nome do jogo
    else:
        with open('preferencia.json','r') as preferencia:
            info = json.load(preferencia)
            
            #fechando o arquivo
            preferencia.close()
            
            #info tem o nome do jogo
            return info

#Abrir arquivo json de estoque

with open('derulo.json','r') as derulo:
    #data['estoque'] é o dicionario que contem os jogos
    data = json.load(derulo)
    
    #Fechando o arquivo
    derulo.close()

#Lendo o arquivo JSON de pedido
info = receberPedido()

#info tem o nome do jogo a ser buscado
info = info['nome']

#criando um arquivo JSON de resposta
novo = open('resposta.json','w')

#buscando o jogo no estoque
jogo = buscaJogo(info,data['estoque'])   

#se o jogo for encontrado
if(jogo != -1):
    #escrevendo a mensagem de sucesso no arquivo JSON de resposta
    novo.write("Jogo encontrado\n")
    
#se o jogo não for encontrado 
else:
    #escrevendo a mensagem de o jogo nao existe no estoque no arquivo JSON de resposta
    novo.write("Jogo nao foi encontrado no estoque\n")

#Fecha o arquivo de resposta
novo.close()

#Lendo o arquivo JSON de preferência
pref = receberPreferencia()

#pref tem o nome do jogo a ter preferência pela locadora
pref=pref['nome']

#Acrescentando a preferência de um jogo no estoque
preferenciaJogo(pref,precoPadrao,data['estoque'])

#Atualizando o arquivo JSON de estoque
with open('derulo.json','w') as derulo:
    json.dump(data,derulo,indent=4)

#Fechando o arquivo JSON
derulo.close()

