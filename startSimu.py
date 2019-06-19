import simpy

exec(open('pessoa.py').read())
env = simpy.Environment()
p = Pessoa(env)
env.run()