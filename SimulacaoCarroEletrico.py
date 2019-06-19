import simpy

def carro(env, nome, bcs, tempo_dirigindo, duracao_carga):
    # Simula dirigir até o posto
    yield env.timeout(tempo_dirigindo)
    
    # Requisita um dos pontos de recarga
    print('%s chegando em %d' % (nome, env.now))
    with bcs.request() as req:
        yield req
        
        # Carrega bateria
        print('%s começando a carregar em %s' % (nome, env.now))
        yield env.timeout(duracao_carga)
        print('%s deixando o posto em %s' % (nome, env.now))

env = simpy.Environment()
bcs = simpy.Resource(env,capacity=2)

for i in range(4):
    env.process(carro(env,'Carro %d' % i, bcs, i*2, 5))

env.run()
