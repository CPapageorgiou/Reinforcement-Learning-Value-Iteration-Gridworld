import numpy as np
from GridWorldTwoGold import GridworldTwoGold

# Implementation of value iteration algorithm in a stochastic environment with two pieces of gold.
# Returns the state value under the optimal policy and the optimal policy itself.
def value_iteration_two_gold():
    
    env = GridworldTwoGold()
    v = np.zeros(shape = len(env.all_states))
    policy = np.full(shape = len(env.all_states), fill_value = "n") 
    
    THETA = 1e-10
    d = 1

    while d >= THETA:
        
        d = 0
        for s in env.non_terminal_states:
            k = env.all_states.index(s) # index of s in all_states
            old_value = v[k] # the current value of s.
            new_value = 0
            optimal_action = 0

            for action in env.actions:

                reward_and_position = env.make_step(action, s) # reward and position of the state in a tuple after applying the action.
                reward = reward_and_position[0]
                position_index = env.all_states.index(reward_and_position[1])
                value_at_position = v[position_index]
                value = 0.85 * (reward + value_at_position)
                
                actions_not_examined = [a for a in env.actions if a != action]
                 
                # same as the outer action-loop but with the actions other than the one of the outer action-loop.
                for act in actions_not_examined:

                    rew_and_pos = env.make_step(act, s)
                    rew = rew_and_pos[0]
                    pos_ind = env.all_states.index(rew_and_pos[1])
                    val_at_pos = v[pos_ind]
                    val_to_add = 0.05 * (rew + val_at_pos)
                    value += val_to_add # update vale
               
                if value > new_value:
                    new_value = value
                    optimal_action = action
            
            v[k] = new_value
            policy[k] = optimal_action
            d = max(d, np.abs(old_value - v[k]))
             
    return v[:25],policy[:25]

v,policy = value_iteration_two_gold()
print(policy)