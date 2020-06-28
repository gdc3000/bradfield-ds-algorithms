"""
Running time of startswith function:
    -2 args: string, prefix
    -Ideal approach:
        -Think about how you might implement
        -Then answer question of running time for how you'd code it up
    -Naive approach: Google it
    -Source code:
        -github cpython

Recursive memory usage:
    -factorial(n)
"""
def factorial_1(n):
    assert n > 0
    if n == 1:
        return 1
    return n * factorial_1(n-1)

def factorial_2(n, result=1):
    assert n > 0
    if n == 1:
        return result
    return factorial_2(n-1, n * result)

"""
Call stack for factorial_1:
f(5)
    5*f(4)
        4*f(3)
            3*f(2)
                2*f(1)
                    1
                2
            6
        24
    120

Multiplications of way back up 

How much space does it take?
    -Depends on how deep the stack gets
    -When finished with recurive call, you can take it off the stack
        -This happens as you come up the stack
    
Call stack for factorial_2:
f(5,1)
    f(4,5)
        f(3,20)
            f(2,60)
                f(1,120)
                    120
                120
            120
        120
    120

This approach does multiplication on way down
Using "tail call optimization", the 2nd one is more efficient, since the state of each recursive call doesn't need to be maintained.
    -This is language specific
    -Not supported by Python
"""
"""
Fibonacci
 n = (n-1) * (n-2)
 -Memory depends on depth of tree, since not all nodes in the call stack need to be kept at the same time.
 -Time is exponential.
"""
"""
What's the point of Big O notation?
-efficiency, big jumps as n-> inf
-independent of systems
-trade-offs given constraints
-concise

What are the downsides of Big O notation?
-can oversimplify, e.g. 2n^2 + 1000000000
-sometimes we know n will be small, not inf
-max size
-readability/maintainability
-assumes worst possible inputs: worst case vs. average case
-architecture level
"""
"""
Examples: 
1) find first index where element in appears in list
    -"Linear in size of array (n)"
    -scan list element-by-element -> O(n)
    -best case: O(1)
    -worst case: O(n)

2) Counting inversions
    -inversion is pair that is out of order
    -Ex: [2,3,1] -> 2,1; 3,1 -> 2 inversions
    -Ex: [3,2,1] -> 3,2; 3,1; 2,1 -> 3 inversions

    naive approach:
        for i=0; i<n;i++
            for j=1+1;j<n;j++
                if a[i] > a[j]
                    c++
        return c
    Answer: O(n^2)
    Signs:
        -2 for loops (nested). good heuristic
        -can think about this algebraically and geometrically
3) "Find_maximum"
    -Tells me maximum value of array
    -Built-in max function
    -Not O(1) since need to know runtime of built-in MAX
4) "Copy a function" - see below
"""
def copy_array(arr):
    copy = []
    for x in arr:
        #copy = copy + [x] #linear time operation in python
        copy += [x] #O(1) time
    return copy

from time import time
from random import randint
n=1
while n < 10**6:
    arr = [randint(0,n) for i in range(n)]
    start=time()
    copy=copy_array(arr)
    end=time()
    print('Elapsed time for n = {}: {}'.format(n, end - start))
    n *= 10