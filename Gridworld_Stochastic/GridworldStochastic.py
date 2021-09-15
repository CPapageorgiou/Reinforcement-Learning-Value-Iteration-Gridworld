import numpy as np

class GridworldStoch:
    
    def __init__(self, num_rows = 5, num_cols = 5, gold_reward = 10, bomb_reward = -10):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.gold_reward = gold_reward
        self.bomb_reward = bomb_reward
        self.gold_positions = np.array([23])
        self.bomb_positions = np.array([18])

        self.actions = ["n", "e", "s", "w"]
        self.num_fields = self.num_cols * self.num_rows
        
        self.rewards = np.full(shape = self.num_fields, fill_value = -1, dtype=np.int)
        self.rewards[self.bomb_positions] = self.bomb_reward
        self.rewards[self.gold_positions] = self.gold_reward
        
        self.all_states = np.arange(0,self.num_fields)
        self.non_terminal_states = np.delete(self.all_states,[self.bomb_positions,self.gold_positions])
    
    # determine the new position and the reward based on the current position.
    def make_step(self, action, agent_position):

        old_position = agent_position
        new_position = agent_position
        if action == "n":
            candidate_position = old_position + self.num_cols
            if candidate_position < self.num_fields:
                new_position = candidate_position
        elif action == "e":
            candidate_position = old_position + 1
            if candidate_position % self.num_cols > 0:  
                new_position = candidate_position
        elif action == "s":
            candidate_position = old_position - self.num_cols
            if candidate_position >= 0:
                new_position = candidate_position
        elif action == "w":  
            candidate_position = old_position - 1
            if candidate_position % self.num_cols < self.num_cols - 1:
                new_position = candidate_position
        else:
            raise ValueError('Action was mis-specified!')

        # calculate reward.
        reward = self.rewards[new_position]
        if new_position in np.append(self.bomb_positions, self.gold_positions):
            reward -= 1

        return reward,new_position