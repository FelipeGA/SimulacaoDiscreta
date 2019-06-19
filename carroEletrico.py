import simpy

class Carro(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        print('Começa a estacionar e a carregar em ',self.env.now)
        duracao_recarga = 5
        yield self.env.process(self.carga(duracao_recarga))

        print('Começa a dirigir em ',self.env.now)
        duracao_viagem = 2
        yield self.env.timeout(duracao_viagem)

    def carga(self,duracao):
        yield self.env.timeout(duracao)

env = simpy.Environment()
carro = Carro(env)
env.run(until=15)