class Carro(env):
    def __init__(self, env):
        self.frequencia = 3
        self.env = env
        self.env.proccess(self.run())

    def run(self):
        while True:
            yield self.env.timeout(self.frequencia)
            print('Carro passou em: ',self.env.now)