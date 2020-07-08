import numpy as np
from pprint import pprint

def min_cost(N: int, h: list) -> int:
    memo = np.empty((N, N))

    #We will use zero indexing and assume the first 
    #stone starts at index 0
    #the row, i, represents the starting point
    #the column, j, represents the ending point
    for i in range(0, N):
        for j in range(i, i+3):
            if j < N:
                if i == 0:
                    min_to_date = 0
                elif i == 1:
                    min_to_date = memo[i-1,i]
                else:
                    min_to_date = min(memo[i-2,i], memo[i-1,i])
                jump_cost = abs(h[i] - h[j])
                memo[i, j] = min_to_date + jump_cost

    return memo[N-1,N-1]

assert min_cost(N=4, h=[10,30,40,20]) == 30
assert min_cost(N=2, h=[10,10]) == 0
assert min_cost(N=6, h=[30, 10, 60, 10, 60, 50]) == 40