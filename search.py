
import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def dfs(problem):
    # Initialize the queue using the already-built in util.py package
    Stack = util.Stack()

    # Initialize the set of Visited Cells, which we use to keep track of which cells we've visited
    VisitedCells = []

    # Get the Starting Cell, using the command that is already built into the project.
    StartCell = problem.getStartState()

    # Initialize the Starting Pair, which could be something like ( [3,2], [] ).  In other words, the
    # start cell is [3,2] and the second entry is [] since we don't have to do anything to get to [3,2].

    StartPair = [StartCell, []]
    Stack.push(StartPair)

    while not Stack.isEmpty():

        CurrentPair = Stack.pop()

        CurrentCell = CurrentPair[0]
        DirectionsToCell = CurrentPair[1]

        if problem.isGoalState(CurrentCell):

            return DirectionsToCell

        else:
            if CurrentCell not in VisitedCells:
                VisitedCells.append(CurrentCell)
                SuccessorList = problem.getSuccessors(CurrentCell)
                #print(CurrentCell, SuccessorList)


                for Child in SuccessorList:
                    #print("child",Child)

                    if Child[0] not in VisitedCells:
                        directions = [Child[1]]
                        # Merge directions from parent state and child state and get directions for child
                        Childpair = (Child[0], DirectionsToCell + directions)
                        #print(Child)
                        Stack.push(Childpair)

    return []



def bfs(problem):
    """Search the shallowest nodes in the search tree first."""
    # Initialize the queue using the already-built in util.py package
    Queue = util.Queue()

    # Initialize the set of Visited Cells, which we use to keep track of which cells we've visited
    VisitedCells = []

    # Get the Starting Cell, using the command that is already built into the project.
    StartCell = problem.getStartState()

    # Initialize the Starting Pair, which could be something like ( [3,2], [] ).  In other words, the
    # start cell is [3,2] and the second entry is [] since we don't have to do anything to get to [3,2].

    StartPair = [StartCell, []]
    Queue.push(StartPair)

    while not Queue.isEmpty():

        CurrentPair = Queue.pop()

        CurrentCell = CurrentPair[0]
        DirectionsToCell = CurrentPair[1]

        if problem.isGoalState(CurrentCell):

            return DirectionsToCell

        else:
            if CurrentCell not in VisitedCells:
                VisitedCells.append(CurrentCell)
                SuccessorList = problem.getSuccessors(CurrentCell)

                for Child in SuccessorList:
                    if Child[0] not in VisitedCells:
                        directions = [Child[1]]
                        # Merge directions from parent state and child state and get directions for child
                        Childpair = (Child[0], DirectionsToCell + directions)
                        Queue.push(Childpair)

    return []



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Initialize the queue using the already-built in util.py package
    PriorityQueue = util.PriorityQueue()

    # Initialize the set of Visited Cells, which we use to keep track of which cells we've visited
    VisitedCells = []

    # Get the Starting Cell, using the command that is already built into the project.
    StartCell = problem.getStartState()

    # Initialize the Starting Pair, which could be something like ( [3,2], [] ).  In other words, the
    # start cell is [3,2] and the second entry is [] since we don't have to do anything to get to [3,2].
    StartCost = 0
    StartPair = [StartCell, [], StartCost]
    PriorityQueue.push(StartPair, StartCost)

    while not PriorityQueue.isEmpty():

        CurrentPair = PriorityQueue.pop()
        CurrentCell = CurrentPair[0]
        DirectionsToCell = CurrentPair[1]

        if problem.isGoalState(CurrentCell):
            return DirectionsToCell

        else:
            if CurrentCell not in VisitedCells:
                VisitedCells.append(CurrentCell)
                SuccessorList = problem.getSuccessors(CurrentCell)

                for Child in SuccessorList:
                    if Child[0] not in VisitedCells:
                        directions = [Child[1]]
                        CurrentCost = CurrentPair[2] + Child[2]
                        # Merge directions and cost from parent state and child state and get directions and cost for child
                        Childpair = [Child[0], DirectionsToCell + directions, CurrentCost]
                        PriorityQueue.push(Childpair, CurrentCost)


    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic ):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Initialize the queue using the already-built in util.py package
    PriorityQueue = util.PriorityQueue()

    # Initialize the set of Visited Cells, which we use to keep track of which cells we've visited
    VisitedCells = []

    # Get the Starting Cell, using the command that is already built into the project.
    StartCell = problem.getStartState()

    # Initialize the Starting Pair, which could be something like ( [3,2], [] ).  In other words, the
    # start cell is [3,2] and the second entry is [] since we don't have to do anything to get to [3,2].
    StartCost = 0
    StartPair = [StartCell, [], StartCost]
    PriorityQueue.push(StartPair, StartCost + heuristic(StartCell, problem))

    while not PriorityQueue.isEmpty():

        CurrentPair = PriorityQueue.pop()
        CurrentCell = CurrentPair[0]
        DirectionsToCell = CurrentPair[1]



        if problem.isGoalState(CurrentCell):
            return DirectionsToCell

        else:
            if CurrentCell not in VisitedCells:
                VisitedCells.append(CurrentCell)
                SuccessorList = problem.getSuccessors(CurrentCell)

                for Child in SuccessorList:
                    if Child[0] not in VisitedCells:
                        directions = [Child[1]]
                        CurrentCost = CurrentPair[2] + Child[2]
                        # Merge directions and cost from parent state and child state and get directions and cost for child
                        Childpair = [Child[0], DirectionsToCell + directions, CurrentCost]
                        # Add heuristic cost to currentcost in order to get cost for child.
                        PriorityQueue.push(Childpair, CurrentCost + heuristic(Child[0], problem))


    return []

class HamiltonianCycle():
    def __init__(self, problem):
        self.x = [-1] * problem.getGridSize()
        self.problem = problem


        self.n = problem.getGridSize()
        # print(problem.getGrid())
        # print(problem.getGridSize())

        # get the adjacency metrix
        self.g = []

        for cell in problem.getGrid():
            adjT = []
            child = [problem.getSuccessors(cell)[i][0] for i in range(len(problem.getSuccessors(cell)))]

            # print(child)
            for adjCell in problem.getGrid():

                if adjCell in child:
                    # print("adjcell")
                    adjT.append(1)
                else:
                    adjT.append(0)

            self.g.append(adjT)



    def hamicycle(self):
        self.x[0] = 0

        if self.hamCycleUtil(1) == False:
            print("Solution does not exist\n")
            return False


        return self.x

    def hamCycleUtil(self, cell):

        if cell == self.n:
            if self.g[self.x[cell - 1]][self.x[0]] == 1:
                #print("reached end")
                return True
            else:
                #print("exited at end")
                return False

        for adjcell in range(1,self.n):
            #print(cell, adjcell)
            if self.canTake(adjcell, cell) == True:
                self.x[cell] = adjcell
                #print(self.x[cell])

                if self.hamCycleUtil(cell+1) == True:
                    #print("true")
                    return True

                self.x[cell] = -1
        #print("exited here")
        return False

    def canTake(self, adjcell, cell):
        if self.g[self.x[cell-1]][adjcell] == 0:
            return False

        for c in self.x:
            if c == adjcell:
                return False
        #print("vertex approved")
        return True

    # def hamiltoniancycle(self):
    #     k = 0
    #     self.x[0] = 0
    #
    #
    #     while(True):
    #         self.nextVertex(k)
    #         if self.x[k] == 0:
    #             print("ended")
    #             return
    #         if k == self.n:
    #             print(self.x)
    #         else:
    #             k = k + 1
    #             self.hamiltoniancycle(k)
    #
    #     print(self.x)
    #
    # def nextVertex(self, k):
    #     print("started with", self.x[k])
    #     count = 1
    #     while (True):
    #         #print(self.x[k])
    #         self.x[k] = int((self.x[k] + 1) % (self.n))
    #         print("x",self.x)
    #         if self.x[k] == 0:
    #             print("ended with self.x[k] == 0", self.x[k],k)
    #             return
    #
    #         #print("count",count)
    #         count = count + 1
    #         #print("X[k-1]:",self.x[k - 1], " X[k]:", self.x[k], "")
    #         #print(self.g[self.x[k - 1]][self.x[k]])
    #         if self.g[self.x[k - 1]][self.x[k]] != 0:
    #             for j in range(1, k-1):
    #                 if self.x[j] == self.x[k]:
    #                     break;
    #                 if j == k:
    #                     if (k < self.n or k == self.n) and (self.g[self.x[self.n]][self.x[1]] != 0):
    #                         print("ended with special", self.x[k])
    #                         return;


