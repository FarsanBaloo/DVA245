# 
# For DVA245 by Anna Friebe, January 2023 

from collections import deque


def merge(S1, S2):
    """Merge two sorted queue instances S1 and S2.
       Result is returned in a new sorted queue.
       Leaves S1 and S2 empty.
       Queues are deques used with the front to the left."""
    # TODO add the functionality that merges S1 and S2 into S
    S = deque()
    while S1 and S2:
        if S1[0] <= S2[0]:
            S.append(S1.popleft())
        else:
            S.append(S2.popleft())
    while S1:
        S.append(S1.popleft())
    while S2:
        S.append(S2.popleft())
    return S


def merge_level_queues(level_queues):
    """Merge the sorted queues in level_queues two by two
    into a new queue with about half the number of sorted 
    queues. level_queues is left empty."""
    next_level_queues = deque()
    # TODO add the functionality that merges the queues of level_queues
    while len(level_queues) > 1:
        q1 = level_queues.popleft()
        q2 = level_queues.popleft()
        next_level_queues.append(merge(q1, q2))
    if len(level_queues) > 0:
        next_level_queues.append(level_queues.popleft())
    # into next_level_queues
    return next_level_queues
  

def merge_sort(S):
    """Sort the elements of queue S using the merge-sort algorithm.
    The sorted result is returned in a new queue, S is left empty
    Queues are deques used with the front to the left. """
    # TODO: 1. Create the level queue.
    level_queues = deque()

    # TODO: Create a queue for each input element and add them to the level_queues
    for element in S:
        level_queues.append(deque([element]))

    # TODO: while we have more than one queue remaining, merge a level
    while len(level_queues) >1:
        level_queues = merge_level_queues(level_queues)

    # TODO: dequeue and return the single remaining merged queue
    if len(level_queues) == 1:
        level_queues = level_queues.popleft()
    return level_queues








