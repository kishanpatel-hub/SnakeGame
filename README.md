# SnakeGame

## Introduction

Snake game is the standard computer game where the player playing the game controls the snake of the game to move and eat the food. Our game consists of the snake travelling on a square floor, without biting itself, attempting to eat as many foods as possible. New food is put on the board when the snake consumes food, and the length of the snake increases by one unit. If the snake has no choice but to bite itself the game is over and the final score is returned. Finally, we calculate the score as the amount of food consumed by the snake or the length of the snake. 4 main constraints of this game are listed below.

1. The goal of this game is to make the snake eat as many foods possible, keeping in mind that the snake does not bite himself. 

2. The snake can move in all 4 directions i.e. left, right, up, down. However, as the snake will have a tail, some directions will not be possible to travel, for example, if the snake is travelling left he can not travel in the opposite direction right. He will have to take the U-turn to travel right.
3. The snake grows by one unit when he eats the food.
4. Once the snake eats the food, the new food is randomly placed in the available space of the square floor. Space which is occupied by the snake is not considered as available space. 

## Agents

### Breadth-first search

Breadth-first search, along with each of the other search algorithms, begins at a random node representing a square in the grid, and upon being placed there, the algorithm searches each successor of the current node next. It then evaluates which node would allow for the best move then, and it proceeds by searching that node and repeating this process. 

![alt text](https://github.com/kishanpatel-hub/SnakeGame/blob/main/Res/BFS-final.gif)

To evaluate the best node for the next action, BFS algorithm creates a path from the current location of the head of the snake to food location and follows that path. Advantage of using BFS is that it always finds the shortest path available but the disadvantage is that it doesn’t plan for the possible deadlock situation thus it might get trapped between its own body.

### Depth-first search

Depth-first search searches through each successor to its furthest depth to check if there is a successful state that can be reached. Upon failure, it backtracks to that node and chooses a different successor to repeat the same process. 

![alt text](https://github.com/kishanpatel-hub/SnakeGame/blob/main/Res/DFS-final.gif)

To evaluate the best node for the next action, DFS algorithm creates a path from the current location of the head of the snake to food location and follows that path. Advantage of using DFS is that it always finds the path available but the disadvantage is that path is not always optimal and it doesn’t plan for the possible deadlock situation thus it might get trapped between its own body.


### Uniform Cost Search


Uniform-cost search is trivial compared to other typical UCS algorithms because each path to a successor is given a cost of 1, so there is no difference in the decision of which path the algorithm will choose and the algorithm essentially shrinks down to is breadth-first search. 

![alt text](https://github.com/kishanpatel-hub/SnakeGame/blob/main/Res/UCS-final.gif)

As UCS algorithm is the same as BFS, it also has the same limitations as the BFS algorithm. 

### A* Search

Our A* search uses a heuristic in determining which successor to follow to minimize the cost to the successor state. In our implementation, our heuristic is Manhattan distance. So to choose best possible action, our A* agent runs the A* algorithm which finds the distance between the head of snake and food at each step and defines the path that can be followed to reach the food.

![alt text](https://github.com/kishanpatel-hub/SnakeGame/blob/main/Res/A-final.gif)

Limitation of A* agent is that as it relies on Manhattan distance for the heuristic, it doesn't really account for the body of the snake and soon runs into a wall or snake body as the length of snake increases.

### Hamiltonian Cycle

If a graph is given then we have to start from some starting vertex and visit all the vertices exactly once and return to the starting vertex so that forms a cycle. So first we need to check is there any hamiltonian cycle possible in a graph, if possible then what is a cycle and if there are multiple cycles we have to find out all those cycles. There are two ways to implement the hamiltonian cycle, the first one is the naive algorithm which starts generating all available vertices configurations and prints a configuration that meets the constraints provided. The second one is Backtracking algorithm which starts with adding vertex 0 in the array of the path, then adds the next vertex 1 but before doing that it checks whether it is adjacent to the previously added vertex and also that it is not present in the array already. We repeat this process until we come up with the cycle. If the cycle is found it is proven that the hamiltonian cycle is possible if not found then it proves that the particular graph does not support the hamiltonian cycle.

![alt text](https://github.com/kishanpatel-hub/SnakeGame/blob/main/Res/Hamiltonian-cycle.gif)

So in our project, we have implemented the backtracking algorithm. There is an array path. So the main function of this array is to add the successors to make a path for the snake. It starts by adding the first successors and then adds the next successors if they are adjacent to the previous one. So in general terms is follows the pattern of DFS. After adding if he reaches the case where he cannot find the next successors it backtraces and looks for the different successors such that they do have adjacent successors. It also checks the condition that if the successor is already present in the path it will not add it. So now from the explanation, we understand that the snake will traverse in the same path throughout the game. One thing to notice is that even if the food is right next to the snake’s mouth rather than just eating it, the snake will traverse the entire path. This can be considered as one of the limitations of the Hamiltonian cycle. So to improve this, we have calculated the score in such a way that whenever the snake takes 1 step, 1 point is deducted from the total score, which means the living reward for the snake is -1. 

### Reinforcement Learning

The machine learning approach that we implemented for the snake game to be able to solve itself is a type of reinforcement learning called Q-learning. This type of algorithm learns what the best action would be in any possible state of the game, and by doing so can understand and execute the ideal sequence of actions to achieve the best score possible. The way that it compares the actions and deciphers which action would be best is by assigning a reward to any action taken, and then evaluating which action would yield the best reward from the current state and allow the current Q value to be as high as it possibly can be. After each reward is reaped, the current Q value is updated to proceed with the next steps. Below, we have attached a photo of the generic equation used in Q-Learning to evaluate actions and their presumed states against one another:

![alt text](https://github.com/kishanpatel-hub/SnakeGame/blob/main/Res/Capture.JPG)

The result of the equation (the new Q value) is in direct correlation with the current Q value and the reward of the action taken. Furthermore, the new Q value is also dependent on the potential of future reward once the action is taken. 

The reason why we chose to implement this type of algorithm is that the concepts of the actions and states fit very well with the snake game. In the snake game, the food is placed at a certain location on the grid (the environment) and similarly, the snake (the agent) is also at a location on the grid. The snake then has up to 4 actions that it could take to get from the current state to the next. The result of any action will lead to either a better state that is closer to winning the game or a state that is not as good and is further from winning. We can define rewards for these actions to find the best possible action that will lead to a better state for each stage of the game. This will now be explained more specifically below. 

The way it works is that there are two main aspects of the game, the grid (which is the environment) and the snake (which is the agent). Each move that the snake makes in the grid represents a new state in the game. Based on how good of a move it was, the state is given a reward which would be higher for better moves and lower for moves that are not as good. The agent then learns which moves would maximize the reward received in every possible state. It is then able to decide which move to make in each given state to maximize the reward at the end of the game.

For purposes of simplicity, we have opted to keep our grid to a size of 3x3, and we removed the aspect of a tail so that the game could have an easier and quicker time with the learning process. In our implementation, we stored the reward of each possible action in each possible state of the game for each possible food location, dependent on where the agent (snake) is located. This screenshot specifies this idea: 

Furthermore, the way that the agent learns these states and can draw these conclusions is because we run 5000 iterations of the game, meaning the game is being played 5000 times. Each time the game is played, dependent on the state of the game, a certain Q value is given and stored for the states that the snake comes across. The snake eventually learns which action would lead to the best reward depending on these given Q values and stores the results, and given that we are doing 5000 iterations of the game, we can rest assured that each state and its best possible action will be defined. 

Learning rate for these iterations was kept at 0.1 as we are already running 5000 iterations and it was expected that it would fail a lot. We help the learning rate low to have less input from previous iterations. And the discount factor was kept at 0.9 to keep the positive impact a little longer. Optimal learning rate and discount rate are yet to be determined as it involves a lot of testing.

## Results

The result was extracted from the program why running each agent for 100 iterations and in each iteration score, length of snake and time taken to complete one game was recorded. Here score is calculated with the living reward of -1 and food reward of +100. Which means the longer it takes to reach food, the lower the score gets and makes it easy to evaluate each of these algorithms. 100 iterations were performed to get the average results of each of the agents. 

![alt text](https://github.com/kishanpatel-hub/SnakeGame/blob/main/Res/Result.JPG)


![alt text](https://github.com/kishanpatel-hub/SnakeGame/blob/main/Res/Score_Result.JPG)

![alt text](https://github.com/kishanpatel-hub/SnakeGame/blob/main/Res/Length_result.JPG)

![alt text](https://github.com/kishanpatel-hub/SnakeGame/blob/main/Res/Time_Result.JPG)




### DFS

From the table below, we can see that the score of Depth-first search is lower than Breadth-first search because it does not consider the shortest path every time which means that it loses points though the average length is approximately the same as BFS. This can be reflected in the time taken column as it takes more time to traverse to the longest path. 

### BFS and UCS

The only difference between BFS and UCS is the cost factor. Now that in our project the cost factor is 1 we can say that BFS and UCS are similar. But due to some randomness, we can see from the table that UCS is performing better than BFS. 


### A* Search

A* uses a heuristic called Manhattan distance. The reason why A* is getting the low score is that it not only looks at the cost factor but also sees the Manhattan distance. And Manhattan distance sometimes is across the snake body and so it deviates to the snake body and happens to bite itself. And hence that is the reason why the average score is low.

### Hamiltonian Cycle

As the snake is completing the entire grid, it can score the best. But at the same time due to the entire traversal over the grid, the snake is taking the highest amount of time to score these points.


 



## Future Work

For the future work, we plan to improve Q learning agent by improving reward function to incorporate more realistic reward for each step to improve its performance. We also plan to add more complexity to model by increasing the grid size and dynamic snake length.

Moreover, in terms of the Hamiltonian cycle, we will work in designing the agent in such a way that it works for nXn grid where n = odd number.
