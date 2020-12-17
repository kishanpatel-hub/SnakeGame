import random

import pygame
from pygame.locals import *
from Snake import Game as game
from QSnake import Game as Qgame
import search
import Qlearning
import util

class randomAgent(search.SearchProblem):

    def __init__(self):
        self.env = Qgame()
        self.env.reset()
        self.action = -1
        while True:

            # do it! render the previous view
            action = random.randrange(0, 3)
            # print("Food: ", problem.getGame().getFood())
            self.env.render()

            done = self.env.step(action)
            # print("Food: ", problem.getGame().getFood(), problem.getStartState())
            # print(env.getFood(), env.getLose(), env.getReward())

            if done:
                break;

class humanAgent(search.SearchProblem):

    def __init__(self):
        self.env = game()
        self.env.reset()
        action = -1
        while True:

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        action = 0

                    elif event.key == K_DOWN:
                        action = 1

                    elif event.key == K_LEFT:
                        action = 2

                    elif event.key == K_RIGHT:
                        action = 3

            # do it! render the previous view
            # action = random.randrange(0, 3)
            self.env.render()
            done = self.env.step(action)
            # print()

            if done:
                break;

class dfsAgent(search.SearchProblem):

    def __init__(self):
        self.env = game()
        self.env.reset()
        self.action = -1
        done = 0


        while True:
            suc = self.getSuccessors(self.getStartState())

            if len(suc) < 1:
                #print("lose")
                self.env.setlose()
                done = True
                #step = random.randrange(0, 3)
                #self.env.step(step)
            else:
                step = random.choice(suc)
                self.env.step(step[1])


            path = search.dfs(self)
            for action in path:
                # do it! render the previous view
                self.env.render()
                done = self.env.step(action)
                # print(env.getFood(), env.getLose(), env.getReward())

            if done:
                break;


    def getStartState(self):
        return self.env.getSnake()[0]

    def getName(self):
        return "Depth First Search"

    def getLose(self):
        return self.env.lose

    def getReward(self):
        return self.env.getReward()

    def getSnake(self):
        return self.env.getSnake()

    def isGoalState(self, cell):
        #print("Food: ",self.env.getFood())
        return cell == self.env.getFood()

    def getSuccessors(self, cell):
        directionVectors = {1:(0,1),0:(0,-1),3:(1,0),2:(-1,0)}

        x = cell[0]
        y = cell[1]

        grid = self.env.getGrid()
        directions = []
        for key in directionVectors.keys():
            if (x+directionVectors[key][0]) < 0:
                continue
            if (x+directionVectors[key][0]) > grid[0]:
                continue
            if (y+directionVectors[key][1]) < 0:
                continue
            if (y+directionVectors[key][1]) > grid[1]:
                continue
            else:
                directions.append([(x + directionVectors[key][0], y + directionVectors[key][1]), key])

        for direction in directions:

            if direction[0] in self.env.getSnake():
                directions.remove(direction)
                continue

        return directions

class bfsAgent(search.SearchProblem):

    def __init__(self):
        self.env = game()
        self.env.reset()
        self.action = -1
        done = 0


        while True:
            suc = self.getSuccessors(self.getStartState())

            if len(suc) < 1:
                self.env.setlose()
                done = True
                # step = random.randrange(0, 3)
                # self.env.step(step)
            else:
                step = random.choice(suc)
                self.env.step(step[1])

            path = search.bfs(self)
            for action in path:
                # do it! render the previous view
                self.env.render()
                done = self.env.step(action)
                # print(env.getFood(), env.getLose(), env.getReward())

            if done:
                break;


    def getStartState(self):
        return self.env.getSnake()[0]

    def getLose(self):
        return self.env.lose

    def getName(self):
        return "Breadth First Search"

    def getReward(self):
        return self.env.getReward()

    def getSnake(self):
        return self.env.getSnake()

    def isGoalState(self, cell):
        #print("Food: ",self.env.getFood())
        return cell == self.env.getFood()

    def getSuccessors(self, cell):
        directionVectors = {1:(0,1),0:(0,-1),3:(1,0),2:(-1,0)}

        x = cell[0]
        y = cell[1]

        grid = self.env.getGrid()
        directions = []
        for key in directionVectors.keys():
            if (x+directionVectors[key][0]) < 0:
                continue
            if (x+directionVectors[key][0]) > grid[0]:
                continue
            if (y+directionVectors[key][1]) < 0:
                continue
            if (y+directionVectors[key][1]) > grid[1]:
                continue
            else:
                directions.append([(x + directionVectors[key][0], y + directionVectors[key][1]), key])

        for direction in directions:

            if direction[0] in self.env.getSnake():
                directions.remove(direction)
                continue

        return directions

class ucsAgent(search.SearchProblem):

    def __init__(self, costFn = lambda x: 1):
        self.env = game()
        self.env.reset()
        self.action = -1
        self.costFn = costFn



        while True:
            suc = self.getSuccessors(self.getStartState())

            if len(suc) < 1:
                self.env.setlose()
                done = True
                # step = random.randrange(0, 3)
                # self.env.step(step)
            else:
                step = random.choice(suc)
                self.env.step(step[1])

            path = search.uniformCostSearch(self)
            for action in path:
                # do it! render the previous view
                self.env.render()
                done = self.env.step(action)
                # print(env.getFood(), env.getLose(), env.getReward())

            if done:
                break;

    def getStartState(self):
        return self.env.getSnake()[0]

    def getName(self):
        return "Uniform Cost Search"

    def getLose(self):
        return self.env.lose

    def getReward(self):
        return self.env.getReward()

    def getSnake(self):
        return self.env.getSnake()

    def isGoalState(self, cell):
        #print("Food: ",self.env.getFood())
        return cell == self.env.getFood()

    def getSuccessors(self, cell):
        directionVectors = {1:(0,1),0:(0,-1),3:(1,0),2:(-1,0)}

        x = cell[0]
        y = cell[1]

        grid = self.env.getGrid()
        directions = []
        for key in directionVectors.keys():
            if (x+directionVectors[key][0]) < 0:
                continue
            if (x+directionVectors[key][0]) > grid[0]:
                continue
            if (y+directionVectors[key][1]) < 0:
                continue
            if (y+directionVectors[key][1]) > grid[1]:
                continue
            else:
                cost = self.costFn(cell)
                directions.append([(x + directionVectors[key][0], y + directionVectors[key][1]), key, cost])

        for direction in directions:

            if direction[0] in self.env.getSnake():
                directions.remove(direction)
                continue

        return directions



class astarAgent(search.SearchProblem):

    def __init__(self, costFn = lambda x: 1):
        self.env = game()
        self.env.reset()
        self.action = -1
        self.costFn = costFn


        while True:
            suc = self.getSuccessors(self.getStartState())

            if len(suc) < 1:
                self.env.setlose()
                done = True
                # step = random.randrange(0, 3)
                # self.env.step(step)
            else:
                step = random.choice(suc)
                self.env.step(step[1])

            path = search.aStarSearch(self, manhattanHeuristic)
            for action in path:
                # do it! render the previous view
                self.env.render()
                done = self.env.step(action)
                # print(env.getFood(), env.getLose(), env.getReward())

            if done:
                break;

    def getStartState(self):
        return self.env.getSnake()[0]

    def getName(self):
        return "A* Search"

    def getLose(self):
        return self.env.lose

    def getGoal(self):
        return self.env.getFood()

    def getReward(self):
        return self.env.getReward()

    def getSnake(self):
        return self.env.getSnake()

    def isGoalState(self, cell):
        #print("Food: ",self.env.getFood())
        return cell == self.env.getFood()

    def getSuccessors(self, cell):
        directionVectors = {1:(0,1),0:(0,-1),3:(1,0),2:(-1,0)}

        x = cell[0]
        y = cell[1]

        grid = self.env.getGrid()
        directions = []
        for key in directionVectors.keys():
            if (x+directionVectors[key][0]) < 0:
                continue
            if (x+directionVectors[key][0]) > grid[0]:
                continue
            if (y+directionVectors[key][1]) < 0:
                continue
            if (y+directionVectors[key][1]) > grid[1]:
                continue
            else:
                cost = self.costFn(cell)
                directions.append([(x + directionVectors[key][0], y + directionVectors[key][1]), key, cost])

        for direction in directions:

            if direction[0] in self.env.getSnake():
                directions.remove(direction)
                continue

        return directions

class HamiltonianAgent(search.SearchProblem):

    def __init__(self):

        self.env = game()
        self.env.reset()
        self.action = -1
        done = False
        h = search.HamiltonianCycle(self)

        path = h.hamicycle()
        path.append(path[0])
        #print(path)
        directions = []
        for cell in path:
            #print(self.getGrid()[cell])
            directions.append(self.getGrid()[cell])
        #print(directions)
        #print(len(directions))


        i = 0

        while(True):
            suc = self.getSuccessors(self.getStartState())
            # print(directions[i], self.getStartState())
            #print(i, len(directions))
            if i >= len(directions)-1:
                i = 0
            if directions[i] == self.getStartState():
                #print("hello")
                for s in suc:
                    #print(s[0], i+1)
                    #print(directions[i+1])
                    if s[0] == directions[i + 1]:
                        self.env.render()
                        #print(s[1])
                        if len(self.env.getSnake()) == self.getGridSize() - 1:
                            self.env.setlose()
                        done = self.env.step(s[1])
                        # if done:
                        #     print(done)
                        #print(done)
            i = i + 1
            if done:
                 break;


    def getStartState(self):
        return self.env.getSnake()[0]

    def getName(self):
        return "Hamiltonian Cycle"

    def getLose(self):
        return self.env.lose

    def getReward(self):
        return self.env.getReward()

    def getLongestpathlength(self):
        x = self.env.getGrid()[0] + 1
        y = self.env.getGrid()[1] + 1
        return (x * y) - len(self.env.getSnake()) + 1

    def getGridX(self):
        return int(self.env.getGrid()[0] + 1)

    def getGridY(self):
        return int(self.env.getGrid()[1] + 1)

    def getGrid(self):
        G = []
        for i in range(self.getGridX()):
            for j in range(self.getGridY()):
                G.append((i, j))
        return G

    def getGridSize(self):
        x = self.env.getGrid()[0] + 1
        y = self.env.getGrid()[1] + 1
        return int(x * y)

    def getGoalState(self):
        #print("Food: ",self.env.getFood())
        return self.env.getSnake()[-1]

    def getSnake(self):
        return self.env.getSnake()

    def getSuccessors(self, cell):
        directionVectors = {1:(0,1),0:(0,-1),3:(1,0),2:(-1,0)}

        x = cell[0]
        y = cell[1]

        grid = self.env.getGrid()
        directions = []
        for key in directionVectors.keys():
            if (x+directionVectors[key][0]) < 0:
                continue
            if (x+directionVectors[key][0]) > grid[0]:
                continue
            if (y+directionVectors[key][1]) < 0:
                continue
            if (y+directionVectors[key][1]) > grid[1]:
                continue
            else:
                directions.append([(x + directionVectors[key][0], y + directionVectors[key][1]), key])

        # for direction in directions:
        #
        #     if direction[0] in self.env.getSnake():
        #         directions.remove(direction)
        #         continue

        return directions

class QlearningAgent(search.SearchProblem):

    def __init__(self):

        self.env = Qgame()
        self.env.reset()
        self.action = -1
        done = False
        Q = Qlearning.Qlearning(self)

        while(True):
            # suc = self.getSuccessors(self.getStartState())
            #
            # if len(suc) < 1:
            #     print("lose")
            #     self.env.setlose()
            #     done = True
            #     # step = random.randrange(0, 3)
            #     # self.env.step(step)
            # else:
            #     step = random.choice(suc)
            #     #print(step)
            #
            #     self.env.render()
            #     self.env.step(step[1])

            self.env.render()
            currentstate = self.getGrid().index(self.getStartState())
            food = self.getGrid().index(self.env.getFood())
            actions = Q[food][currentstate]
            action = actions.index(max(actions))
            # print(action, self.getStartState())
            previouscell = self.env.getSnake()[0]

            done = self.env.step(action)
            print(previouscell, action, self.env.getSnake()[0], self.env.getFood())

            if done:
                break;



    def getStartState(self):
        return self.env.getSnake()[0]

    def getEnv(self):
        return self.env

    def getReward(self):
        return self.env.getReward()

    def getLongestpathlength(self):
        x = self.env.getGrid()[0] + 1
        y = self.env.getGrid()[1] + 1
        return (x * y) - len(self.env.getSnake()) + 1

    def getGridX(self):
        return int(self.env.getGrid()[0] + 1)

    def getGridY(self):
        return int(self.env.getGrid()[1] + 1)

    def getGrid(self):
        G = []
        for i in range(self.getGridX()):
            for j in range(self.getGridY()):
                G.append((i, j))
        return G

    def getGridSize(self):
        x = self.env.getGrid()[0] + 1
        y = self.env.getGrid()[1] + 1
        return int(x * y)

    def getGoalState(self):
        #print("Food: ",self.env.getFood())
        return self.env.getSnake()[-1]

    def getSuccessors(self, cell):
        directionVectors = {1:(0,1),0:(0,-1),3:(1,0),2:(-1,0)}

        x = cell[0]
        y = cell[1]

        grid = self.env.getGrid()
        directions = []
        for key in directionVectors.keys():
            if (x+directionVectors[key][0]) < 0:
                continue
            if (x+directionVectors[key][0]) > grid[0]:
                continue
            if (y+directionVectors[key][1]) < 0:
                continue
            if (y+directionVectors[key][1]) > grid[1]:
                continue
            else:
                directions.append([(x + directionVectors[key][0], y + directionVectors[key][1]), key])

        for direction in directions:

            if direction[0] in self.env.getSnake():
                directions.remove(direction)
                continue

        return directions



def manhattanHeuristic(position, problem, info={}):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.getGoal()
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

def euclideanHeuristic(position, problem, info={}):
    "The Euclidean distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.getGoal()
    return ( (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 ) ** 0.5