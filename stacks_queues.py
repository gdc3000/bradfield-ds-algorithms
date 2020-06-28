"""
Write a function that uses a stack to return a reversed copy 
of a list. We will re-use the stack given here: https://bradfieldcs.com/algos/stacks/implementation/
as a starting point.

Implementation idea: One solution here would be to load
list items into a stack one-by-one, removing each item
from the beginning of the list. Once the list is empty, 
you'd pop items from the stack into a list copy, appending
each item to the list.
"""
class Stack:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.insert(0, item)

    def pop(self):
        return self._items.pop(0)

    def peek(self):
        return self._items[0]

    def size(self):
        return len(self._items)


def reverse_list(lst: list) -> list:
    s = Stack()
    i = 0
    out = []
    while i < len(lst):
        s.push(lst[i])
        i+=1
    while not s.is_empty():
        out.append(s.pop())
    return out

"""
Implement a queue using stacks. Solution below has same 
interface as queue implementation in algos.

One solution would be to simply add items to a stack during the 
enqueue step. During dequeue, you would remove all items 
from this original stack and load them one-by-one into another
temp stack, thus putting the last-in items on the bottom 
and first-in items on top. You could then pop() the first-in item from
this temp stack to be returned. Prior to returning it, it is important to rebuild
the original stack (without the first-in item to be returned).
"""

class Stack_Queue:

    def __init__(self):
        self.stack = Stack()

    def is_empty(self):
        return self.stack.is_empty()

    def enqueue(self, item):
        self.stack.push(item)

    def dequeue(self):
        temp = Stack()
        while not self.stack.is_empty():
            t = self.stack.pop()
            temp.push(t)
        out = temp.pop()
        while not temp.is_empty():
            t = temp.pop()
            self.stack.push(t)
        return out

    def size(self):
        return self.stack.size()

"""
The solution above is O(1) for enqueue operations, but T(n) = 2*n for dequeue, thus it
is O(n) for all dequeue operations. You could likely make it more efficient by
storing the temp "queue" stack after any dequeue() and re-using it during 
subsequent dequeue operations if no enqueue operations were performed in
between. Thus, subsequent dequeues would be O(1) unless an enqueue was 
performed in between.
"""

