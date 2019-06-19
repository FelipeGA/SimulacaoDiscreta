import simpy

def Pessoa(env):
    def __init__(self,env):
        self.env = env
        self.env.process(self.run())
    
    def run(self):
        while True:
            print('Começou a estudar em: ', self.env.now)
            tempEstudo = 2
            yield self.env.timeout(tempEstudo)

            print('Iniciou as redes sociais em: ',self.env.now)
            tempRedes = 5
            yield self.env.timeout(tempRedes)