import sys
import gym

def load_env(env_name):
    env = gym.make(env_name)
    env.reset()
    for _ in range(1000): # run for 1000 steps
        env.render()
        action = env.action_space.sample() # pick a random action
        env.step(action) # take action

if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 2):   # if argument is not equal to 2
        print 'Usage: python %s environment_name' % argvs[0]
        quit()
        
    load_env(argvs[1])    

    
