import simpy
import pessoa

exec(open('pessoa.py').read())
env = simpy.Environment()
p = Pessoa(env)
env.run(until=20)