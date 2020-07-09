import numpy as np
from pprint import pprint

def min_cost(N: int, h: list) -> int:
    if N < 2:
        return 0

    #each element in the list represents the min cost of getting from the beginning to that element
    cost = [None] * N
    cost[0] = 0
    cost[1] = abs(h[0] - h[1])
    for i in range(2, N):
        single_jump = abs(h[i] - h[i-1]) + cost[i-1]
        double_jump = abs(h[i] - h[i-2]) + cost[i-2]
        cost[i] = min(single_jump, double_jump)

    return cost[N-1]

assert min_cost(N=4, h=[10,30,40,20]) == 30
assert min_cost(N=2, h=[10,10]) == 0
assert min_cost(N=6, h=[30, 10, 60, 10, 60, 50]) == 40