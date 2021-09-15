import numpy as np
from GridworldStochastic import GridworldStoch 

# Implementation of value iteration algorithm in a stochastic environment. 
# Returns the state value under the optimal policy and the optimal policy itself.
def value_iteration_stoch():
    
    env = GridworldStoch()
    v = np.zeros(shape = env.num_fields)
    policy = np.full(shape = env.num_fields, fill_value = "n") 
    
    THETA = 1e-10
    d = 1
    
    while d >= THETA:
        
        d=0
        for s in env.non_terminal_states:
            old_value = v[s]
            new_value = 0
            optimal_action = 0

            for action in env.actions:

                reward_and_position = env.make_step(action, s) # reward and position of the state in a tuple after applying the action.
                reward = reward_and_position[0]
                value_at_position = v[reward_and_position[1]]
                value = 0.85 * (reward + value_at_position)
                actions_not_examined = [a for a in env.actions if a != action]
                
                # same as the outer action-loop but with the actions other than the one of the outer action-loop.
                for act in actions_not_examined:

                    rew_and_pos = env.make_step(act, s)
                    rew = rew_and_pos[0]
                    val_at_pos = v[rew_and_pos[1]]
                    val_to_add = 0.05 * (rew + val_at_pos)
                    value += val_to_add
  
                if value > new_value:
                    new_value = value
                    optimal_action = action

            v[s] = new_value
            policy[s] = optimal_action

            d = max(d, np.abs(old_value - v[s]))

    return v,policy

v,policy = value_iteration_stoch()

