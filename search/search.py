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

def getActionFromFinalNodeList(l,visited,parent_child):
    listofMove=[]
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    for z in l:  
        if(visited[z][0]=="South" or visited[z][0]=="North" or visited[z][0]=="East" or visited[z][0]=="West" or
           visited[z][0]=="down" or visited[z][0]=="up" or visited[z][0]=="right" or visited[z][0]=="left"): 
            previous = l[l.index(z)-1]
            if z in parent_child.keys():
                for search in parent_child[z]:
                    if search[0]==previous:
                        if search[1]=="South":
                            listofMove.append(n)
                        elif search[1]=="North":
                            listofMove.append(s)
                        elif search[1]=="East":
                            listofMove.append(w)    
                        elif search[1]=="West":
                            listofMove.append(e) 
                        elif search[1]=="up":
                            listofMove.append("down")
                        elif search[1]=="down":
                            listofMove.append("up")
                        elif search[1]=="left":
                            listofMove.append("right")    
                        elif search[1]=="right":
                            listofMove.append("left") 
                    
        else:
            if isinstance(visited[z], list):
                for i in visited[z]:
                    if l[l.index(z)-1] in i:
                        listofMove.append(i)
            elif visited[z]=="None":
                    continue
            else:       
                listofMove.append(visited[z])        
    return  listofMove     
    

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
   
    openList = util.Stack()
    openList.push(problem.getStartState())
    closedList = util.Stack()
    listofMove = []
    visited = {}
    parent_child = {}
    visited[problem.getStartState()] = "None"
    while not openList.isEmpty():
        x = openList.pop()
        if problem.isGoalState(x):
            closedList.push(x)
            break
        else:
            child = problem.getSuccessors(x)
            closedList.push(x)
            if len(child)!=0:
                ch =[]
                for c in child:
                    ch.append(c)
                    if c[0] not in visited.keys():
                        openList.push(c[0])
                        visited[c[0]] = c[1]
                    else:
                        value = visited[c[0]]
                        temp=[]
                        if value!="None" :
                            if isinstance(value, list):
                                temp.extend(value)
                            else:
                                temp.append(value)
                            temp.append(c[1])
                            visited[c[0]] = temp
                parent_child[x] = ch
            else:
                parent_child[x] = []
           
    
    l = []
    
    def ischild(x1,x2):
        if problem.isGoalState(x2):
           if x1 not in l:
               l.append(x1)
           l.append(x2)
           return
       
        child = [x[0] for x in parent_child[x1]]
       
        if x2 in child:
           if x1 not in l: l.append(x1)
           ischild(x2,closedList[closedList.index(x2)+1])
        else:
           if x1 in l: l.remove(x1)
           ischild(closedList[closedList.index(x1)-1],x2)
    
    closedList = closedList.list
    ischild(closedList[0],closedList[1])

    return getActionFromFinalNodeList(l,visited,parent_child)
                
            

def breadthFirstSearch(problem):
    "*** YOUR CODE HERE ***"
    openList = util.Queue();
    openList.push(problem.getStartState())
    closedList = util.Queue();
    listofMove = []
    visited = {}
    parent_child = {}
    visited[problem.getStartState()] = "None"
    while not openList.isEmpty():
        x = openList.pop()
        if problem.isGoalState(x):
            closedList.push(x)
            break
        else:
            child = problem.getSuccessors(x)
            closedList.push(x)
            if len(child)!=0:
                ch =[]
                for c in child:
                    ch.append(c)
                    if c[0] not in visited.keys():
                        openList.push(c[0])
                        visited[c[0]] = c[1]
                    else:
                        value = visited[c[0]]
                        temp=[]
                        if value!="None":
                            if isinstance(value, list):
                                temp.extend(value)
                            else:
                                temp.append(value)
                            temp.append(c[1])
                            visited[c[0]] = temp
                parent_child[x] = ch
            else:
                parent_child[x] = []
    
    closedList = closedList.list
    cyclePath = []
    l = []
   
    def cycle(child,):
            for c in child:
                if not problem.isGoalState(c):
                    if c in parent_child.keys():
                       for z in parent_child[c]:
                           if z[0] in child:
                               if z[0] in l:
                                   return True
    def ischild(x1,x2):
        if problem.getStartState() == x2:
            if x1 not in l:
                l.append(x1)
            l.append(x2)
           
            child = [x[0] for x in parent_child[x2]]
 
            if len(child)>1:
                for c in child:
                    if not problem.isGoalState(c):
                        if c in parent_child.keys():
                           for z in parent_child[c]:
                               if z[0] in child:
                                   cyclePath.append(c)                    
            return
        
        child = parent_child[x2]
        temp=[]
        for x in child:
            temp.append(x[0])
        child = temp
        if x1 in child:
                if x1 not in l:
                    l.append(x1)
                if len(child)>1:
                    for c in child:
                        if not problem.isGoalState(c):
                            if c in parent_child.keys():
                                for z in parent_child[c]:
                                    if z[0] in child:
                                        if z[0] in l:  
                                            cyclePath.append(c)
                ischild(x2,closedList[closedList.index(x2)+1])
                temp=[]       
        else:
            if x1 in l:
                l.remove(x1)
            ischild(x1,closedList[closedList.index(x2)+1])
       
    
    ischild(closedList[0],closedList[1])
    for x in cyclePath:
        if x in l:
            l.remove(x)
    
    return getActionFromFinalNodeList(l[::-1],visited,parent_child)     
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    openList = util.PriorityQueue();
    openList.push(problem.getStartState(),0)
    closedList = util.Queue();
    listofMove = []
    visitedNodes = []
    visited = {}
    parent_child = {}
    dist_from_root = {}
    dist_from_root[problem.getStartState()] = 0
    visited[problem.getStartState()] = "None"
    while not openList.isEmpty():
        x = openList.pop()
        if problem.isGoalState(x):
            visitedNodes.append(x)
            break
        else:
            visitedNodes.append(x)
            child = problem.getSuccessors(x)    
            closedList.push(x)
            if len(child)!=0:
                ch =[]
                for c in child:
                    ch.append(c)
                    if c[0] not in visited.keys():
                        openList.update(c[0],dist_from_root[x]+c[2])
                        dist_from_root[c[0]] = dist_from_root[x]+c[2]
                        visited[c[0]] = c[1]
                    else:
                        value = visited[c[0]]
                        temp=[]
                        if value!="None":
                            if isinstance(value, list):
                                temp.extend(value)
                            else:
                                temp.append(value)
                            temp.append(c[1])
                            temp = list(set(temp))
                            if len(temp)==1:
                                visited[c[0]] = temp[0]
                            else:
                                visited[c[0]] = temp
                parent_child[x] = ch
            else:
                parent_child[x] = []
                
    visitedNodes = visitedNodes[::-1]
    cyclePath = []
    l = []

    def ischild(x1,x2):
        print(x1,x2)
        if problem.getStartState() == x2:
            if x1 not in l:
                l.append(x1)
            l.append(x2)
            temp=[]
            child = parent_child[x2]
            for x in child:
                temp.append(x[0])
            child = temp
            if len(child)>1:
                for c in child:
                    if not problem.isGoalState(c):
                        if c in parent_child.keys():
                           for z in parent_child[c]:
                               if z[0] in child:
                                   cyclePath.append(c)                    
            return
        child = parent_child[x2]
        temp=[]
        for x in child:
            temp.append(x[0])
        child = temp
        if x1 in child:
                if x1 not in l:
                    l.append(x1)
                if len(child)>1:
                    for c in child:
                        if not problem.isGoalState(c):
                            if c in parent_child.keys():
                                for z in parent_child[c]:
                                    if z[0] in child:
                                        if z[0] in l:  
                                            cyclePath.append(c)
                ischild(x2,visitedNodes[visitedNodes.index(x2)+1])      
        else:
            if x1 in l:
                l.remove(x1)
            ischild(x1,visitedNodes[visitedNodes.index(x2)+1])
       
    
    ischild(visitedNodes[0],visitedNodes[1])
    for x in cyclePath:
        if x in l:
            l.remove(x)
    l = l[::-1]
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    #print(l)
    for z in l:
        if(visited[z][0]=="South" or visited[z][0]=="North" or visited[z][0]=="East" or visited[z][0]=="West"): 
            previous = l[l.index(z)-1]
            for search in parent_child[z]:
                if previous in search:
                    if search[1]=="South":
                        listofMove.append(n)
                    elif search[1]=="North":
                        listofMove.append(s)
                    elif search[1]=="East":
                        listofMove.append(w)
                    elif search[1]=="West":
                        listofMove.append(e)
        else:
            if isinstance(visited[z], list):
                previous = l[l.index(z)-1]
                for search in parent_child[previous]:
                    if search[0]==z:
                        listofMove.append(search[1])
            elif visited[z]=="None":
                continue
            else:
                listofMove.append(visited[z])

    return listofMove 
   

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    openList = util.PriorityQueue();
    openList.push(problem.getStartState(),0)
    opennlist = []
    opennlist.append(problem.getStartState())
    closedList = []
    listofMove = []
    parent_child = {}
    dist_from_root = {}
    dist_from_root[problem.getStartState()] = 0
    parent_child[problem.getStartState()] = problem.getStartState()
    all_child_of_parent = {}
    while not openList.isEmpty():   
        q = openList.pop()
        if problem.isGoalState(q):
            new_path=[]
            while parent_child[q] != q:
                new_path.append(q)
                q = parent_child[q]
            
            new_path.append(problem.getStartState())
            new_path.reverse()
            x1 = new_path[0]
            x2 = new_path[1]
            while(True):
                for x,y in all_child_of_parent[x1]:
                    if x==x2:
                        listofMove.append(y)
                if problem.isGoalState(x2):
                    break
                x1 = x2
                x2 = new_path[new_path.index(x2)+1]
            return listofMove
        children = []
        closedList.append(q)
        for x,y,z in problem.getSuccessors(q):
            children.append((x,y))
            if x not in opennlist and x not in closedList:
                openList.update(x, dist_from_root[q]+z+heuristic(x, problem))
                opennlist.append(x)
                dist_from_root[x] = dist_from_root[q]+z
                parent_child[x] = q
            else:
                if dist_from_root[x]>dist_from_root[q]+z:
                    dist_from_root[x] = dist_from_root[q]+z
                    parent_child[x] = q
                    if x in closedList:
                        closedList.remove(x)
                        openList.update(x,dist_from_root[q]+z+heuristic(x, problem))
                        opennlist.append(x)
                    else:
                        openList.update(x,dist_from_root[q]+z+heuristic(x, problem))
        all_child_of_parent[q] = children
        

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
