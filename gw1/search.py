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
from game import Directions
from typing import List

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




class Node:
    """
    Search node object for your convenience.

    (Added for CSEN 266 from the Berkeley CS188 "Search and Games" release that the
    Group Homework 1 handout was written against.)

    This object uses the state of the node to compare equality and for its hash function,
    so you can use it in things like sets and priority queues if you want those structures
    to use the state for comparison.

    Example usage:
    >>> S = Node("Start", None, None, 0)
    >>> A1 = Node("A", S, "Up", 4)
    >>> B1 = Node("B", S, "Down", 3)
    >>> B2 = Node("B", A1, "Left", 6)
    >>> B1 == B2
    True
    >>> A1 == B2
    False
    >>> node_list1 = [B1, B2]
    >>> B1 in node_list1
    True
    >>> A1 in node_list1
    False
    """
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.state == other.state

    def __ne__(self, other):
        return self.state != other.state


def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
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
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    # Debugging print statements left in place

    # VISITED SET: A set that stores the tuples representing the coordinates of visited nodes
    visited = set()

    # FRONTIER: A BFS uses a FIFO queue to explore nodes and then expands from their neighbors
    frontier = util.Queue()
    # States are saved as coordinate tuples e.g. (5, 5)
    start = Node(problem.getStartState(), None, None, 0)
    # Prime the frontier and visited set with the start node
    frontier.push(start)
    visited.add(start.state)
    # print("Starting BFS with start state:", problem.getStartState())

    while not frontier.isEmpty():
        current = frontier.pop()
        if problem.isGoalState(current.state):
            # PATH: Once BFS finds the goal, we need to backtrack by following the parent pointers
            # from the goal node back to the start node.
            path = []
            cost = 0
            while current.parent is not None:
                path.append(current.action)
                cost += current.path_cost
                current = current.parent
            # We need to reverse the lsit because we constructed it from the goal to the start
            # Path should be from the start to the goal.
            # Note: The GW1 document suggests to use path.insert(0, action). Choosing to reverse
            # because constantly inserting to the front of a list in python is inefficient.
            # Inserting to the front of a Python list is O(n) operation but we do it N times
            # which leads to a runtime complexity of O(n^2) for constructing the path.
            # Reversing the list is an O(n) operation.
            # Alternatively, use a deque and use appendLeft to construct the path
            return path[::-1]

        # SUCCESSORS: The successor of the current node gets added to the frontier
        # The successors are added to the visited set when they are pushed into the frontier
        # THe successors are returned by passing the current state to problem.getSuccessors()
        for successor, action, step_cost in problem.getSuccessors(current.state):
            if successor not in visited:
                visited.add(successor)
                frontier.push(Node(successor, current, action, step_cost))

    # If the frontier is empty and no goal has been found, return an empty path
    return []
    

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
