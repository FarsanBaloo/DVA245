# 
# For DVA245 by Anna Friebe, January 2023 

from collections import deque


def merge(S1, S2):
    """Merge two sorted queue instances S1 and S2.
       Result is returned in a new sorted queue.
       Leaves S1 and S2 empty.
       Queues are deques used with the front to the left."""
    S = deque()
    # TODO add the functionality that merges S1 and S2 into S
    return S
  
def merge_level_queues(level_queues):
    """Merge the sorted queues in level_queues two by two
    into a new queue with about half the number of sorted 
    queues. level_queues is left empty."""
    next_level_queues = deque()
    # TODO add the functionality that merges the queues of level_queues
    # into next_level_queues
    return next_level_queues
  

def merge_sort(S):
    """Sort the elements of queue S using the merge-sort algorithm.
    The sorted result is returned in a new queue, S is left empty
    Queues are deques used with the front to the left. """
    level_queues = deque()
    # TODO: Create a queue for each input element and add them to the level_queues
    # TODO: while we have more than one queue remaining, merge a level 
    # TODO: dequeue and return the single remaining merged queue

