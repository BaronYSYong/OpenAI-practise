from gym import envs

env_list = envs.registry.all()
"""
[EnvSpec(DoubleDunk-v0), EnvSpec(InvertedDoublePendulum-v0), 
EnvSpec(BeamRider-v0), EnvSpec(Phoenix-ram-v0), EnvSpec(Asterix-v0), 
EnvSpec(TimePilot-v0), EnvSpec(Alien-v0), EnvSpec(Robotank-ram-v0), 
EnvSpec(CartPole-v0), EnvSpec(Berzerk-v0), EnvSpec(Berzerk-ram-v0), 
EnvSpec(Gopher-ram-v0), ...
"""

for n in env_list:
    print str(n)[8:-1]
