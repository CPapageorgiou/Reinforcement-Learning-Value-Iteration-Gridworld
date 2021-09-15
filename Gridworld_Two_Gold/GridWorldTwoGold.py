import numpy as np

# class for the gridworld enviroment with two pieces of gold.
class GridworldTwoGold:
    
    def __init__(self, num_rows = 5, num_cols = 5, gold_reward = 10, bomb_reward = -10, regular_reward = -1):
        self.num_rows = num_rows
        self.num_cols = num_cols 
        self.gold_reward = gold_reward
        self.bomb_reward = bomb_reward
        self.regular_reward = regular_reward
        self.gold_positions = np.array([12,23])
        self.bomb_positions = np.array(18)
           
        self.actions = ["n", "e", "s", "w"]
        self.num_fields = self.num_cols * self.num_rows
        
        # produce all valid states.
        self.all_states_provisional = [(i,j,k) for k in range(2) for j in range(2) for i in range (25) if ( k!= 1 or j != 1)]               
        self.unreachable_states = [(23,1,0),(12,0,1)]
        self.all_states = [(i[0],1,1) if i in self.unreachable_states else i for i in self.all_states_provisional ]
        
        # terminal and non terminal states.
        self.gold_terminal_states = [(i,1,1) for i in self.gold_positions]   
        self.bomb_terminal_states = [(18,0,0),(18,1,0),(18,0,1)]        
        self.terminal_states = self.gold_terminal_states + self.bomb_terminal_states
        self.non_terminal_states = [(x) for x in self.all_states if x not in self.terminal_states]
        
        # states through which gold can be collected with one move.
        self.special_states_actions_gold12 = [("e",(11,0,0)),("e",(11,0,1)), ("w",(13,0,0)), ("w",(13,0,1)),("n",(7,0,0)),("n",(7,0,1)), ("s",(17,0,0)),("s",(17,0,1))] 
        self.special_states_actions_gold23 = [("e",(22,0,0)),("e",(22,1,0)), ("w",(24,0,0)),("w",(24,1,0))]
        self.special_states_actions = self.special_states_actions_gold12 + self.special_states_actions_gold23
      
    # determine the new position and the reward based on the current position.
    def make_step(self, action, current_position):

        old_position = current_position
        new_position = current_position
        reward = 0
        
        # current position is not a state from which the agent can move to a gold position.
        if (action, current_position) not in self.special_states_actions:
            
            if action == "n":
                candidate_position = self.add_elementwise(old_position,(self.num_cols,0,0))
                if candidate_position[0] < self.num_fields:
                    new_position = candidate_position
            elif action == "e":
                candidate_position = self.add_elementwise(old_position,(1,0,0))
                if candidate_position[0] % self.num_cols > 0:
                    new_position = candidate_position
            elif action == "s":
                candidate_position = self.add_elementwise(old_position,(-self.num_cols,0,0))
                if candidate_position[0] >= 0:
                    new_position = candidate_position
            elif action == "w": 
                candidate_position = self.add_elementwise(old_position, (- 1,0,0))
                if candidate_position[0] % self.num_cols < self.num_cols - 1:
                    new_position = candidate_position
            else:
                raise ValueError('Action was mis-specified!')

        # current position is a state from which the agent can move to gold position 12.
        # If evaluates to true then gold exists at gold position 12 (haven't been collected yet) and needs to be collected.
        elif (action, current_position) in self.special_states_actions_gold12:
            
            reward += self.gold_reward # get the reward.
        
            
            if action == "n":
                candidate_position = self.add_elementwise(old_position,(self.num_cols,1,0))
                if candidate_position[0] < self.num_fields:
                    new_position = candidate_position
            elif action == "e":
                candidate_position = self.add_elementwise(old_position,(1,1,0))
                if candidate_position[0] % self.num_cols > 0: 
                    new_position = candidate_position
            elif action == "s":
                candidate_position = self.add_elementwise(old_position,(-self.num_cols,1,0))
                if candidate_position[0] >= 0:
                    new_position = candidate_position
            elif action == "w":  # "LEFT"
                candidate_position = self.add_elementwise(old_position, (- 1,1,0))
                if candidate_position[0] % self.num_cols < self.num_cols - 1:
                    new_position = candidate_position
            else:
                raise ValueError('Action was mis-specified!')
                
        # current position is a state from which the agent can move to gold position 23. 
        # If evaluates to true then gold exists at gold position 23 (haven't been collected yet) and needs to be collected.        
        elif (action, current_position) in self.special_states_actions_gold23:
                         
            reward += self.gold_reward # get the reward
            
            if action == "n":
                candidate_position = self.add_elementwise(old_position,(self.num_cols,0,1))
                if candidate_position[0] < self.num_fields:
                    new_position = candidate_position
            elif action == "e":
                candidate_position = self.add_elementwise(old_position,(1,0,1))
                if candidate_position[0] % self.num_cols > 0:
                    new_position = candidate_position
            elif action == "s":
                candidate_position = self.add_elementwise(old_position,(-self.num_cols,0,1))
                if candidate_position[0] >= 0:
                    new_position = candidate_position
            elif action == "w":  # "LEFT"
                candidate_position = self.add_elementwise(old_position, (- 1,0,1))
                if candidate_position[0] % self.num_cols < self.num_cols - 1:
                    new_position = candidate_position
            else:
                raise ValueError('Action was mis-specified!')
    
        else: 
            raise ValueError('Wrong input')  
    
        reward += self.regular_reward # reward for the move.
        
        if new_position in self.bomb_terminal_states:
            reward += self.bomb_reward
            
        return reward, new_position
    
    
    def add_elementwise(self,x,y):
        return x[0]+y[0], x[1]+y[1], x[2]+y[2]    
    