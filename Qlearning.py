import random

import pygame
from pygame.locals import *
from QSnake import Game as game

def Qlearning(problem):


    S = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    #S = problem.getGrid()
    print(S)
    #A = ['NORTH', 'WEST', 'SOUTH', 'EAST']
    A = [0,1,2,3]

    #Terminals = [[3, 1], [3, 2]]
    directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]

    Q = [[[[0 for a in A] for s in S] for t in S] for k in range(5001)]

    directionVectors = {1: (0, 1), 0: (0, -1), 3: (1, 0), 2: (-1, 0)}

    k = 0
    Alpha = 0.1
    Gamma = 0.9

    # print(A)
    # print(S)
    # print(directionVectors.keys())

    for k in range(5000):

        # if k < 10 or k == 4999:
        #     print("")
        #     print(k, Q[k])

        for t in S:

            for s in S:
                for key in directionVectors.keys():

                    n = (s[0] + directionVectors[key][0], s[1] + directionVectors[key][1])
                    if n in S:
                        i = S.index(s)
                        f = S.index(t)
                        j = S.index(n)
                        b = A.index(key)


                        # Calculate the sample and update the (k+1)th row of the Q table
                        sample = R(s, key, n, t) + Gamma * max(Q[k][f][j][0], Q[k][f][j][1], Q[k][f][j][2], Q[k][f][j][3])

                        Q[k + 1][f][i][b] = (1 - Alpha) * Q[k][f][i][b] + Alpha * sample

                        if k == 4999:
                            print("food", t, "State", s, "Action", key, "Going", next, "Updated Value", round(Q[k + 1][f][i][b], 5))

    return Q[4999]

def R(s, a, n, f):
    if n == f:
        #print("entered")
        return 1
    else:
        return -1
