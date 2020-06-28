"""
Hashing and binary search both address the same problem: finding an item in a collection. 
What are some trade-offs between the two strategies? 
-Hashing has a higher insertion cost, if there are collisions.
-Hashing also has potential to consume more memory or use memory less efficiently 
  (since values aren't stored sequentially)
-Hashing will generally have better time complexity for search: O(1) vs O(logn)

When might you want to pick one over the other?
-I might pick hashing if I'm not memory constrained and 
 if I have a very large list and/or if I will do frequent lookups
-If I need to update the entire list frequently, I may prefer hashing
-Binary search might be better if I am going to search frequently relative to updates or 
 quick search time are key concern.
-Implementation of binary search may be easier since I don't need to manage collisions
"""

"""
If sorting takes (at minimum) O(n log n) time, and binary search takes O(log n) time, 
under what circumstances might it worth it to sort a collection in order to perform binary search?
-With sort and searching k times: T(k) = n*logn + k*logn
-Without sort and searching k times: T(k) = k*n
-Thus, if I search more than 2*log(n) times per sort, then I'm better of sorting.
"""

"""
Write a plain binary search function
"""
def binary_search(lst, key, start_idx=None, end_idx=None):
    """Accepts a sorted list and key. Returns true if the list contains key (bounded by 
       the start and end indexes, inclusive). Returns false if the bounded list is empty. 
       If neither, it returns results from a recursively callwith narrower indexes."""
    #start out without indices for a new list. This avoids slicing for performance reasons.
    if start_idx is None and end_idx is None:
        start_idx = 0
        end_idx = len(lst) - 1
 
    #base case
    if start_idx > end_idx or end_idx < start_idx:
        return False
    
    #check if key is at middle index. If so return True.
    middle_idx = start_idx + (end_idx - start_idx) // 2
    middle_key = lst[middle_idx]
    if middle_key == key:
        return True

    #reset indexes based on whether value is greater than or less than middle_key
    if key < middle_key:
        start_idx = start_idx
        end_idx = middle_idx - 1
    else:
        start_idx = middle_idx + 1
        end_idx = end_idx
    
    #if element not found and list not empty, return recursive call with updated indexes!
    return binary_search(lst, key, start_idx, end_idx)

test_0 = []
test_3 = [1,2,3]
test_5 = [0,1,2,4,5]
test_6 = [0,1,2,3,4,6]

assert binary_search(test_3,4) == False
assert binary_search(test_3,-1) == False
assert binary_search(test_3,3) == True
assert binary_search(test_5,3) == False
assert binary_search(test_5,0) == True
assert binary_search(test_5,4) == True
assert binary_search(test_5,2) == True
assert binary_search(test_6,2) == True
assert binary_search(test_6,3) == True
assert binary_search(test_6,0) == True
assert binary_search(test_6,5) == False
assert binary_search(test_6,7) == False
assert binary_search(test_6,-1) == False
assert binary_search(test_6,2,1,3) == True
assert binary_search(test_0,1) == False

"""
Course notes (6/18)
Integer overflow can be a concern if middle index 
is calculated: middle_idx = (end_idx + start_idx) // 2 
"""
"""
Problem:
-A bunch of commits 0...9
-Have a function run_test_suite(id) -> bool
-One commit breaks the build
-How do you figure out which commit broke the build?

Solutions:
-Binary search: start in middle
-If not broken, it's somewhere between commit 5 and 9. Try the middle of that range...
-etc...

Class discussion:
-Carefully define gaurantees (https://www.cs.cornell.edu/courses/cs2112/2015fa/lectures/lec_loopinv/):
    -left = not broken, right = broken
    -every loop shrinks the range
-Make sure they hold as you build the loop

if broken(0): return 0
if not broken(n-1): return -1
left = 0
right = n -1
while left + 1 < right:
    mid = left + (right - left) // 2
    if broken(mid):
        right = mid
    else:
        left = mid
return right

"""
"""
Problem: "Square root"
    input: some integer n
    output: smallest value x, s.t. that x^2 > n

Examples:
    25 -> 5
    26 -> 6
    36 -> 6
    100 -> 10
    99 -> 10

Possible solutions:
-Initial conditions:
  -left = 1
  -right = n // 2
-Think about nos and yes's: what is teh question?
    -x^2 > n
-Guarantees:
  -x[left]^2 <= n
  -x[right]^2 > n
-check that can set left to 0 and right to len - 1 and gaurantee will hold
-run constantly shrinking loop. Stop when left + 1 = right
-return right

How to update old code:
-Just change the conditions
-Don't need to get fancy with initial n conditions

Go standard library has generic binary search:
-range (n)
-question to ask (f)
-Ex: sort.Search(n+1, function(x int) bool {return x * x >= n})

Challenge: see if you can implement Go's standard library function in own language

"""
"""
Next problem: Quick sort - Implement function that takes a pivot value, shuffles values so that 
every value <= pivot is before it in new array, everything > pivot is right in new
array.

Assumptions:
-Assume range is not empty

Invariant
-i right of last element <= to pivot
-j > largest element

def partition(array, left, right):
    pivot == array[left]
    i = left + 1
    j = left + 1
"""
"""
Challenge problem:
https://leetcode.com/accounts/login/?next=/contest/weekly-contest-193/problems/minimum-number-of-days-to-make-m-bouquets/
Hint: runtime of O(n*logn) due to expensive question

-Can use generic binary search framework!
"""
