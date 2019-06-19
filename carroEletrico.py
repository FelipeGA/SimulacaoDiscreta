import simpy

class Carro(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        print('Começa a estacionar e a carregar em ',self.env.now)
        duracao_recarga = 5
        try:
           yield self.env.process(self.carga(duracao_recarga))
        except simpy.Interrupt:
            print('Carga interrompida!')

        print('Começa a dirigir em ',self.env.now)
        duracao_viagem = 2
        yield self.env.timeout(duracao_viagem)

    def carga(self,duracao):
        yield self.env.timeout(duracao)

def motorista(env,carro):
    yield env.timeout(3)
    carro.action.interrupt()

env = simpy.Environment()
carro1 = Carro(env)
env.process(motorista(env,carro1))

env.run(until=140)
