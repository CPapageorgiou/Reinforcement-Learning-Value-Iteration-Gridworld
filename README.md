 ## Description
 
 Implementation of the Value Iteration algorithm to compute the optimal policy and each state value under the optimal policy in three variants of a gridworld environment. These are as follows:

<ul>
<li> Deterministic gridworld environment with one piece of gold.
<li> Stochastic gridworld environment with one piece of gold. 
<li> Stochastic gridworld environment with two pieces of gold.
</ul>

<p> In the stochastic environments the agent moves as intended with probability 0.8 and randomly with probability 0.2</p> 

<p>In the evironment with two pieces of gold, the arrays returned specify the expected return and an optimal policy at the corresponding grid sqaure before any pieces of gold are collected or a bomb is activated.
</p>

### Grid World Environment with one piece of gold.

 ![](Images\one_gold_env.png)


### Grid World Environment with two pieces of gold.

 ![](Images\two_gold_env.png)

### Rules
 <strong> Actions available:</strong> The agent has four possible actions in each grid square. These are west, north, south, and east. If the direction of movement is blocked by a wall the agent remains in the same grid square.

<strong>Collecting gold:</strong> On its first arrival at a grid square that contains gold (from a neighbouring grid square), the agent collects the gold. 
Note that, in order to collect the gold, the agent needs to transition into the grid square (containing the gold) from a different grid square.

<strong>Hitting the bomb:</strong> On arrival at a grid square that contains a bomb (from a neighbouring grid square), the agent activates the bomb.

<strong>Terminal states:</strong> The game terminates when all gold is collected or when the bomb is activated.



 ### Value Iteration pseudocode
 Reproduced from the textbook (Reinforcement Learning, Sutton & Barto, 2018, pp. 83).

<img src=Images\value_iteration_pseudocode.png height=200>

The set S contains all non-terminal states, whereas S<sup>+</sup> is the set of all states (terminal and non-terminal). The symbol r represents the immediate reward on transition from state s to the next state s' via action a.

#### Parameters Used
<ul>
<li> Θ = 1×10<sup>−10</sup>.
<li> All initial state values v(s) = 0.
<li> γ = 1.
<li> Reward function:  −1 for each navigation action (including when the action results in hitting the wall), an additional  +10 for collecting each piece of gold, and an additional  −10 for activating the bomb.
</ul>
