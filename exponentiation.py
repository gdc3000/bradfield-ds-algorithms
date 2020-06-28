"""
Warm up problem: write function to raise a to power of b. E.g. power(a, b) -> a^b.

Naive approach:
-Recursively:
-Just return 1 when exponent is zero
-Return 1 when exponent is 1
-Call return a * power(a, b-1)

Smarter approach:
-Observe that a^b = (a^(b/2) * a^(b/2))
"""
import timeit
import numpy as np

#This runs in O(exp(log(n))) time which is approximately O(n)
def power_v1(a: int, b: int) -> int:
    if b == 0:
        return 1
    if b == 1: 
        return a
    return power_v1(a, b // 2) * power_v1(a, b // 2) * power_v1(a, b % 2)

assert power_v1(2,0) == 1
assert power_v1(2,1) == 2
assert power_v1(2,2) == 4
assert power_v1(2,3) == 8
assert power_v1(2,8) == 2**8
assert power_v1(2,90) == 2**90
assert power_v1(3,8) == 3**8

#This runs in log(n) time
def power_v2(a: int, b: int) -> int:
    if b == 0:        return 1
    if b == 1: 
        return a
    x = power_v2(a, b // 2)
    return x * x * power_v2(a, b % 2)

#Look at difference in run time
start_time = timeit.default_timer()
b=200
power_v1(2,b)
v1_time = timeit.default_timer() - start_time
print(v1_time)

start_time = timeit.default_timer()
power_v2(2,b)
v2_time = timeit.default_timer() - start_time
print(v2_time)

print('Log(n) / n: ', np.log(b) / b)
print('Actual: ', v2_time/v1_time)

"""
Next problem: 
-Thanos is attacking an avenger's base.
-Base is n units wide. N is power of 2 (2,4,8,...).
-At each step, Thanos has 2 options:
    1) If region is empty (no Avengers), Thanos can use E energy to destroy region
    2) If region is not empty, Thanos then it costs a * Z * size of region, where Z is the cost
       to take out one Avenger and a is number of Avengers.
-Alternatively, Thanos can split into two regions and attack them separately.

Goal: minimize energy used to take out the base.

f(left, right) -> # of avengers
    where left and right are indexes of region

Given:
    -E, cost to attack empty region
    -Z, cost per avenger for empty region
    -f -> "scan function" that counts avengers in some region
    -n, size of region

Return, min total energy required to take out the entire base

Ideas:
-Base cases:
    -Unit size is one
    -Scan returns empty
-Whole region: calculate cost to attack
-Split: calculate cost to split and attack
-Pursue lowest cost solution
"""

