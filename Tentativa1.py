import simpy
import math
import random

class Carro:
    def __init__(self,env,nome,localizacao,qtde_carga):
        self.env = env
        self.nome = nome
        self.localizacao = localizacao
        self.qtde_carga = qtde_carga

class Posto:
    def __init__(self,env,nome,localizacao,num_tomada):
        self.env = env
        self.nome = nome
        self.localizacao = localizacao
        #Definindo número de tomadas disponíveis no posto
        self.num_tomada = simpy.Resource(env, capacity=num_tomada)
        self.num_tomada_int = num_tomada


    def recarga(self,env,carro):
        yield self.env.timeout(abs(self.localizacao - carro.localizacao) + self.env.now)
        
        #Carga perdida durante trajeto até o posto
        carro.qtde_carga -= abs(self.localizacao - carro.localizacao)
        print('O %s chegou no tempo %d no %s com %d de carga' % (carro.nome,abs(self.localizacao - carro.localizacao),self.nome,carro.qtde_carga))

        with self.num_tomada.request() as tomada:
            yield tomada

            print('O %s começou a carregar no tempo %d' % (carro.nome,self.env.now))
            #Aqui a gente calcula o tempo para recarga total baseado na quantidade de carga atual
            yield self.env.timeout((100 - carro.qtde_carga) * 0.2)

            carro.qtde_carga = 100
            print('O %s terminou a carga no tempo %d' % (carro.nome,self.env.now))

def defCarros(qtde_carros):
    carros = []

    print('Carros do sistema:')
    for i in range(qtde_carros):
        localizacao = random.randint(0,15)
        carga = random.randint(10,70)
        carros.append(Carro(env,'carro%s' % (i+1),localizacao,carga))
        print('Carro%d com %d por cento de carga e localização %d' % (i+1,carga,localizacao))

    print('\n\n')
    
    return carros

env = simpy.Environment()

#Definição dos postos
posto1 = Posto(env, 'posto1', 13, 2)
posto2 = Posto(env, 'posto2', 10, 4)
posto3 = Posto(env, 'posto3', 7, 1)
postos = [posto1,posto2,posto3]

print('Postos do sistema:')
for posto in postos:
    print('%s com %d tomadas e localizado %d' % (posto.nome,posto.num_tomada_int,posto.localizacao))

#Definição dos carros
carros = defCarros(6)

#Verifica qual posto fica mais próximo
for carro in carros:
    menor_dist = math.inf
    for posto in postos:
        if abs(posto.localizacao - carro.localizacao) < menor_dist:
            menor_dist = abs(posto.localizacao - carro.localizacao)
            postoEscolhido = posto
    env.process(postoEscolhido.recarga(env,carro))

env.run()
