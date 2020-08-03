# search.py
# ---------
# Licensing Information: You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

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

    def getSuccessors(self,state):
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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze. For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started,  you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:",  problem.getStartState() ============(5, 5)
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())   ============True
    print "Start's successors:", problem.getSuccessors(problem.getStartState())  ===========[((x1, y1), 'South', 1), ((x2, y2), 'West', 1)]
    """
    "*** YOUR CODE HERE ***"
    from game import Directions

    # Initialization
    # We use a stack for DFS traversal
    # We use a list to keep track of all points that have already been traversed
    fringe = util.Stack()
    visitedList = []

    # Push the starting point into stack
    fringe.push((problem.getStartState(), [], 0))
    # Pop out the point
    (state, toDirection, toCost) = fringe.pop()
    # Add the point to visited list
    visitedList.append(state)

    # Loop continues until we reach the goal point
    while not problem.isGoalState(state):
        # Get all successors to the current point
        successors = problem.getSuccessors(state)
        for point in successors:
            # If the successor has not been visited, we push it into the stack
            if (not point[0] in visitedList):
                fringe.push((point[0], toDirection + [point[1]], toCost + point[2]))
                # Point is added to the visited list to ensure it is not visited again
                visitedList.append(point[0])
        (state, toDirection, toCost) = fringe.pop()

    #List of directions from start point to goal point is returned
    return toDirection

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions

    # Initialization
    # We use a queue for BFS traversal
    # We use a list to keep track of all points that have already been traversed
    fringe = util.Queue()
    visitedList = []

    # Push the starting point into queue
    fringe.push((problem.getStartState(), [], 0))
    # Pop out the point
    (state, toDirection, toCost) = fringe.pop()
    # Add the point to visited list
    visitedList.append(state)

    # Loop continues until we reach the goal point
    while not problem.isGoalState(state):
        # Get all successors to the current point
        successors = problem.getSuccessors(state)
        for point in successors:
            # If the successor has not been visited, we push it into the stack
            if not point[0] in visitedList:
                fringe.push((point[0], toDirection + [point[1]], toCost + point[2]))
                # Point is added to the visited list to ensure it is not visited again
                visitedList.append(point[0])
        (state, toDirection, toCost) = fringe.pop()

    return toDirection



def iterativeDeepeningSearch(problem):
    """This function is for the first of the grad students questions"""
    "*** MY CODE HERE ***"
    from game import Directions

    # Initialization
    # We use a stack for traversal
    # We use a list to keep track of all points that have already been traversed
    fringe = util.Stack()
    depth = 1;

    # Loop continues until we find a solution within the depth 
    while True:
        visitedList = []
        # Push the starting point into stack
        fringe.push((problem.getStartState(), [], 0))
        # Pop out the point
        (state, toDirection, toCost) = fringe.pop()
        # Add the point to visited list
        visitedList.append(state)
        # Loop continues until we reach the goal point
        while not problem.isGoalState(state):
            # Get all successors to the current point
            successors = problem.getSuccessors(state)
            for point in successors:
                # Point is added if it has not been visited and total cost is within the depth
                if (not point[0] in visitedList) and (toCost + point[2] <= depth):
                    fringe.push((point[0], toDirection + [point[1]], toCost + point[2]))
                    # Add this point to visited list
                    visitedList.append(point[0])

            # If the goal point is not found within the current depth, jump out and increase the depth
            if fringe.isEmpty():
                break

            (state, toDirection, toCost) = fringe.pop()

        if problem.isGoalState(state):
            return toDirection

        # Increase the depth
        depth += 1


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions

    # Initialization
    # We use a priority queue for traversal
    # We use a list to keep track of all points that have already been traversed
    fringe = util.PriorityQueue()
    visitedList = []

    # Push the starting point into queue with priority == 0
    fringe.push((problem.getStartState(), [], 0), 0)
    # Pop out the point
    (state, toDirection, toCost) = fringe.pop()
    # Add the point to visited list
    visitedList.append((state, toCost))

    # Loop continues until we reach the goal point
    while not problem.isGoalState(state):
        # Get all successors to the current point
        successors = problem.getSuccessors(state)
        for point in successors:
            visitedExist = False
            total_cost = toCost + point[2]
            for (visitedState, visitedToCost) in visitedList:
                # Point is added only if it has not been visited, or has been visited with a higher cost than the current move
                if (point[0] == visitedState) and (total_cost >= visitedToCost):
                    # Point is recognized as visited
                    visitedExist = True
                    break

            if not visitedExist:        
                # Push the point with priority == total cost
                fringe.push((point[0], toDirection + [point[1]], toCost + point[2]), toCost + point[2])
                # Add this point to visited list
                visitedList.append((point[0], toCost + point[2]))

        (state, toDirection, toCost) = fringe.pop()

    return toDirection

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from game import Directions

    # Initialization
    # We use a priority queue for traversal
    # We use a list to keep track of all points that have already been traversed
    fringe = util.PriorityQueue() 
    visitedList = []

    # Push the starting point into queue with priority == 0
    fringe.push((problem.getStartState(), [], 0), 0 + heuristic(problem.getStartState(), problem))
    # Pop out the point
    (state, toDirection, toCost) = fringe.pop()
    # Add the point to visited list
    visitedList.append((state, toCost + heuristic(problem.getStartState(), problem)))

    # Loop continues until we reach the goal point
    while not problem.isGoalState(state):
        # Get all successors to the current point
        successors = problem.getSuccessors(state)
        for point in successors:
            visitedExist = False
            total_cost = toCost + point[2]
            for (visitedState, visitedToCost) in visitedList:
                # Point is added only if it has not been visited, or has been visited with a higher cost than the current move
                if (point[0] == visitedState) and (total_cost >= visitedToCost):
                    visitedExist = True
                    break

            if not visitedExist:
                # Push the point with priority == total cost
                fringe.push((point[0], toDirection + [point[1]], toCost + point[2]), toCost + point[2] + heuristic(point[0], problem))
                # Add this point to visited list
                visitedList.append((point[0], toCost + point[2]))

        (state, toDirection, toCost) = fringe.pop()

    return toDirection


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
