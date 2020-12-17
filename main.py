# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import agent
import time
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #agent.randomAgent()
    #agent.humanAgent()
    #Agent = agent.dfsAgent()
    #Agent = agent.bfsAgent()
    #Agent = agent.ucsAgent()
    #Agent = agent.astarAgent()
    #Agent = agent.HamiltonianAgent()
    # score = []
    # snakelength = []
    # timetaken = []
    # for i in range(20):
    #     start = time.time()
    #     Agent = agent.QlearningAgent()
    #     if Agent.getLose():
    #         end = time.time()
    #         score.append(Agent.getReward())
    #         snakelength.append(len(Agent.getSnake()))
    #         timetaken.append(end - start)
    #
    # print(Agent.getName(), "  Average Score: ", sum(score) / len(score), "  Average Length: ",
    #       sum(snakelength) / len(snakelength), "  Average Time Taken at 30 FPS: ",
    #       sum(timetaken) / len(timetaken))

    agent.QlearningAgent()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
