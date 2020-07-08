"""
Reminder of water jug problem from last time.
Can think of this as a state machine.

What are states? What are transitions between states?
-Base states of system:
  -object or tuple (two fill levels)
-Operations from each state:
   -fill or empty each jug
   -dump one jug into the other

First question: Can we get 4 gallons in one jug?
   -Traverse through entire graph and see if can satisfy node
   -Can use BFS and traverse through graph iteratively
"""


from collections import deque

def die_hard(cap1, cap2, target):
    """
    Returns a boolean:
        -Can we get target gallons?
    """
    def get_neighbors(curr1, curr2):
        """
        Assume cap1 = 5, cap2 = 2. Suppose we're in a state (0,3)
        e.g. jug1 has 0 gallons
             jug2 has 3 gallons

             (5,3) fill curr1
             (3,0) fill curr1 with curr2
             (0,3) fill curr2 with curr1
             (0,0) empty curr2
        """
        neighbors = []
        # fill a jug
        neighbors.append((cap1, curr2))
        neighbors.append((curr1,cap2))

        # empty a jug
        neighbors.append((0, curr2))
        neighbors.append((curr1, 0))

        # transfer between jugs
        # (5, 0) -> (2, 3)
        # transfer 1 -> 2
        # constrained by capacity of 2, amount in 1
        transfer_1_2 = min(curr1, cap2 - curr2)
        neighbors.append((curr1 - transfer_1_2, curr2 + transfer_1_2))

        # transfer 2 -> 1
        # constrained by capacity of 1, amount in 2
        transfer_2_1 = min(cap1 - curr1, curr2)
        neighbors.append((curr1 + transfer_2_1, curr2 - transfer_2_1))

        return neighbors

    #Traverse the graph
    
    # What exactly does visited mean? Two options:
    # 1) Add something to visited as soon as we add to queue. Never add twice to queue.
    # 2) Visited contains everything we've dequeue and process. If dequeue something twice, "continue" / ignore it
    
    visited_nodes = set()
    q = deque()

    q.append((0, 0))
    visited_nodes.add((0,0)) #Implemented option 1

    while len(q) > 0:
        cur1, cur2 = q.popleft() #pop() would make it depth first search because it uses stack
        if cur1 == target or cur2 == target:
            return True

        for neighbor in get_neighbors(cur1, cur2):
            if neighbor not in visited_nodes:
                q.append(neighbor)
                visited_nodes.add(neighbor)

    # We never encounted target
    return False

print(die_hard(2,6,3))
print(die_hard(5,3,4))
print(die_hard(10,6,8))
print(die_hard(1,2,2))

"""
Modify problem to say shortest distance to problem state
(-1 if not possible)

"""
def die_hard_dist(cap1, cap2, target):
    def get_neighbors(curr1, curr2):
        """
        Assume cap1 = 5, cap2 = 2. Suppose we're in a state (0,3)
        e.g. jug1 has 0 gallons
             jug2 has 3 gallons

             (5,3) fill curr1
             (3,0) fill curr1 with curr2
             (0,3) fill curr2 with curr1
             (0,0) empty curr2
        """
        neighbors = []
        # fill a jug
        neighbors.append((cap1, curr2))
        neighbors.append((curr1,cap2))

        # empty a jug
        neighbors.append((0, curr2))
        neighbors.append((curr1, 0))

        # transfer between jugs
        # (5, 0) -> (2, 3)
        # transfer 1 -> 2
        # constrained by capacity of 2, amount in 1
        transfer_1_2 = min(curr1, cap2 - curr2)
        neighbors.append((curr1 - transfer_1_2, curr2 + transfer_1_2))

        # transfer 2 -> 1
        # constrained by capacity of 1, amount in 2
        transfer_2_1 = min(cap1 - curr1, curr2)
        neighbors.append((curr1 + transfer_2_1, curr2 - transfer_2_1))

        return neighbors

    #Traverse the graph
    
    # What exactly does visited mean? Two options:
    # 1) Add something to visited as soon as we add to queue. Never add twice to queue.
    # 2) Visited contains everything we've dequeue and process. If dequeue something twice, "continue" / ignore it
    
    # Keeping track of distance
    # Option 1: keep distance information in queue
    # Option 2: keep a dict
    q = deque()
    visited_nodes = set()
    
    start = (0, 0)
    q.append((0, start))
    visited_nodes.add((0,0)) #Implemented option 1

    while len(q) > 0:
        d, (cur1, cur2) = q.popleft()
        if cur1 == target or cur2 == target:
            return d

        for neighbor in get_neighbors(cur1, cur2):
            if neighbor not in visited_nodes:
                q.append((d + 1, neighbor))
                visited_nodes.add(neighbor)

    # We never encounted target
    return -1

# (0,0) -> (0,5) -> (3,2) -> (3,3) -> (1,5) -> (0,5) ->
print(die_hard_dist(5,3,4))


"""
How would we return shortest path?
"""
def die_hard_path(cap1, cap2, target):
    def get_neighbors(curr1, curr2):
        """
        Assume cap1 = 5, cap2 = 2. Suppose we're in a state (0,3)
        e.g. jug1 has 0 gallons
             jug2 has 3 gallons

             (5,3) fill curr1
             (3,0) fill curr1 with curr2
             (0,3) fill curr2 with curr1
             (0,0) empty curr2
        """
        neighbors = []
        # fill a jug
        neighbors.append((cap1, curr2))
        neighbors.append((curr1,cap2))

        # empty a jug
        neighbors.append((0, curr2))
        neighbors.append((curr1, 0))

        # transfer between jugs
        # (5, 0) -> (2, 3)
        # transfer 1 -> 2
        # constrained by capacity of 2, amount in 1
        transfer_1_2 = min(curr1, cap2 - curr2)
        neighbors.append((curr1 - transfer_1_2, curr2 + transfer_1_2))

        # transfer 2 -> 1
        # constrained by capacity of 1, amount in 2
        transfer_2_1 = min(cap1 - curr1, curr2)
        neighbors.append((curr1 + transfer_2_1, curr2 - transfer_2_1))

        return neighbors

    #Traverse the graph
    
    # What exactly does visited mean? Two options:
    # 1) Add something to visited as soon as we add to queue. Never add twice to queue.
    # 2) Visited contains everything we've dequeue and process. If dequeue something twice, "continue" / ignore it
    
    # Keeping track of distance
    # Option 1: keep distance information in queue
    # Option 2: keep a dict

    #Keep record of parent of each node.
    q = deque()
    visited_nodes = set()
    parent = dict()
    
    start = (0, 0)
    q.append((0, start))
    visited_nodes.add((0,0)) #Implemented option 1
    parent[start] = None

    while len(q) > 0:
        d, (cur1, cur2) = q.popleft()
        if cur1 == target or cur2 == target:
            path = []
            node = (cur1, cur2)
            while node is not None:
                path.append(node)
                node = parent[node]
            return list(reversed(path))

        for neighbor in get_neighbors(cur1, cur2):
            if neighbor not in visited_nodes:
                q.append((d + 1, neighbor))
                visited_nodes.add(neighbor)
                parent[neighbor] = (cur1, cur2)

    # We never encounted target
    return -1

print(die_hard_path(5,3,4))