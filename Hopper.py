import gym

"""
Source: https://github.com/openai/mujoco-py
30 days free trial license,  https://www.roboti.us/license.html
"""
env = gym.make('Hopper-v1')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
