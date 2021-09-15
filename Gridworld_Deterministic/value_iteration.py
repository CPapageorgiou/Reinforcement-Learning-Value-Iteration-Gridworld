# implementation of the value iteration algorithm. 

import numpy as np
from Gridworld import Gridworld

def value_iterations():
    
    env = Gridworld()
    v = np.zeros(shape = env.num_fields)
    policy = np.full(shape = env.num_fields, fill_value = "n") 
    
    THETA = 1e-10
    d = 1
    value_candidates = []
    iterations =0
    
    while d >= THETA:
        
        d=0
        iterations +=1 
        for s in env.non_terminal_states:
            old_value = v[s]
            new_value = 0
            optimal_action = 0

            for action in env.actions:

                reward_and_position = env.make_step(action, s)
                reward = reward_and_position[0]
                value_at_position = v[reward_and_position[1]]
                value = reward + value_at_position

                if value > new_value:
                    new_value = value
                    optimal_action = action

            v[s] = new_value
            policy[s] = optimal_action

            d = max(d, np.abs(old_value - v[s]))

    return v,policy

v,policy = value_iterations() 
print(v)
print(policy)