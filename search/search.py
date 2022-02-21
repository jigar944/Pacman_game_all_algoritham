# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
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

 

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
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

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
   
    open_list = util.Stack()

    closedList = util.Stack()
    path = []
    action_cost = 0  # Cost of each movement.

    start_position = problem.getStartState()

    # Pushes the start position to the Queue.
    open_list.push((start_position, path, action_cost))

    while not open_list.isEmpty():

        current_node = open_list.pop()
        position = current_node[0]
        path = current_node[1]

        if position not in closedList.list:
            closedList.push(position)

        if problem.isGoalState(position):
            return path

        successors = problem.getSuccessors(position)

        for item in successors:
            if item[0] not in closedList.list:
                new_position = item[0]
                new_path = path + [item[1]]
                open_list.push((new_position, new_path, item[2]))
            
            

def breadthFirstSearch(problem):
    "*** YOUR CODE HERE ***"
    
    open_list = util.Queue()

    closedList = util.Queue()
    path = []
    action_cost = 0  # Cost of each movement.

    start_position = problem.getStartState()

    # Pushes the start position to the Queue.
    open_list.push((start_position, path, action_cost))

    while not open_list.isEmpty():

        current_node = open_list.pop()
        position = current_node[0]
        path = current_node[1]

        if position not in closedList.list:
            closedList.push(position)

        if problem.isGoalState(position):
            return path

        successors = problem.getSuccessors(position)

        for item in successors:
            if item[0] not in closedList.list and item[0] not in (node[0] for node in open_list.list):
                new_position = item[0]
                new_path = path + [item[1]]
                open_list.push((new_position, new_path, item[2]))
                

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    openList = util.PriorityQueue()
    startNode = problem.getStartState()
    cost = 0
    path = []
    openList.push((startNode,path),cost)
    closedList = util.Queue()
    
    while not openList.isEmpty():
        
        current = openList.pop()
        
        current_node = current[0]
        action = current[1]
        
        
        closedList.push(current_node)
        
        if problem.isGoalState(current_node):
            return action
        
        
        successor = problem.getSuccessors(current_node)
        
        for child in successor:
            if child[0] not in closedList.list and (child[0] not in (visited[2][0] for visited in openList.heap)):
                new_path = action + [child[1]]
                new_cost = problem.getCostOfActions(new_path)
                openList.push((child[0],new_path), new_cost)
            elif (child[0] in (visited[2][0] for visited in openList.heap)):
                old_cost = [problem.getCostOfActions(node[2][1]) for node in openList.heap if node[2][0]==child[0]][0]
                new_path = action + [child[1]]
                if old_cost>problem.getCostOfActions(new_path):
                    openList.update((child[0],new_path),problem.getCostOfActions(new_path))
                    
    
   

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    openList = util.PriorityQueue()
    startNode = problem.getStartState()
    cost = 0
    path = []
    openList.push((startNode,path),cost)
    closedList = util.Queue()
    
    while not openList.isEmpty():
        current = openList.pop()
        
        current_node = current[0]
        action = current[1]
        
        closedList.push(current_node)
        
        if problem.isGoalState(current_node):
            return action
              
        successor = problem.getSuccessors(current_node)
        
        for child in successor:
            if child[0] not in closedList.list and (child[0] not in (visited[2][0] for visited in openList.heap)):
                new_path = action + [child[1]]
                new_cost = problem.getCostOfActions(new_path)+heuristic(child[0], problem)
                openList.push((child[0],new_path), new_cost)
            elif (child[0] in (visited[2][0] for visited in openList.heap)):
                old_cost = [problem.getCostOfActions(node[2][1]) for node in openList.heap if node[2][0]==child[0]][0]
                new_path = action + [child[1]]
                if old_cost>problem.getCostOfActions(new_path):
                    new_cost = problem.getCostOfActions(new_path) +heuristic(child[0], problem)
                    openList.update((child[0],new_path),problem.getCostOfActions(new_path))
       

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
