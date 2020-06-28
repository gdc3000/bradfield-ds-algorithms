"""
Problem:
Given a paper strip. n squares wide. 

Want to tile the strip using two types of tiles. 

Cannot have tile hanging off the edge of paper "overflow".

Red pattern: 1 square wide. 
Blue pattern: 2 squares wide.

Examples:
| | | | | | -> |R|R|R|R|R| or |B| |B| |R| or etc.

|B| |B| |B| -> Not allowed ("overflow")

|B| |B| |R| is not equal to |R|B| |B| |, even though counts of red and blue are the same

Question: How many different patterns can you make, given n?

Examples:
n=1: Only red is possible
n=2: 2 red tiles, 1 blue tile

Promise:
-No inputs of zero or negative
-But if zero: what is most useful?
"""
"""
More examples:
n=3:
|R|R|R|
|B| |R|
|R|B| |

n=4:
|R|R|R|R|
|B| |B| |
|R|B| |R|
|R|R|B| |
|B| |R|R|

Potential solutions:
-Start from one end. 
-Function reduces by 1 (R) and reduces by two (B)
-Count++
-Base case: 
  if: size 1, then count++ and end

"""

def pattern_count(n):
    if n == 0:
        return 1
    elif n == 1:
        return pattern_count(n-1)
    elif n > 1:
        return pattern_count(n-1) + pattern_count(n-2)

"""
Problem solving approaches:
-how to model the problem
-try small cases, look for pattern
-base cases + incremental progress
-simplify problem

"Leap of faith"
-Should feel like this but not the reality
"""
"""
Elliot's solution:
-Note than n=1-6 looks like a fibonacci sequence
-Not sure why this is the case or if it will continue to hold

Possible reasons:
n=4
4->3 (R)
  3->2 (R)
    2->1 (R)
      1->0 (R)
    2->0 (B)
  3->1 (B)
    1->0 (R)
4->2 (B)
  2->1 (R)
    1->0 (R)
  2->0 (B)

Elliot's guidance: how do we know it works for any size?
-First solve examples on paper, then prove that solution generalizes
-Notice that it works for 1,2,3
-then notice 5 = 3 + 2, so if 2 and 3 work then 5 must as well
-etc...

Next: turn into code
-This is the easy part because we've put a lot of thought into (1) finding pattern, (2) justifying pattern

How to solve this iteratively?
-Sometimes called "top-down vs bottom-up". He doesn't like this terminology, because this doesn't represent how you solve problems
-Prefers: recursion with memoization vs. building up table gradually
"""
def pattern_count_iter(n):
    arr = [None,1,2]
    while len(arr) < n + 1:
        arr.append(arr[-1] + arr[-2])
    return arr[-1]

"""
Other tips:
-Recommends mentioning packages you could use in an interview. I.e. fibonacci package.
-In terms of clean code: recommends wrapping a package in your own function with good comments.
-Repeated work is the signal of time complexity overhead
    -Notice that constantly recalculating f(3), f(2), etc.
    -Merge sort is an example of recursion without lots repeated work

Best recursion problems to practice:
-Trees and linked lists
    -"Tree picker"
    -e.g. leaves of binary tree, trim leaves off

"""
