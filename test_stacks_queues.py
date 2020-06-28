import pytest
import stacks_queues

lists = [
    ([1,2,3,4,5],[5,4,3,2,1]),
    ([],[]),
    ([1],[1])
]

def test_reverse_list():
    for l in lists:
        before, after = l
        assert stacks_queues.reverse_list(before) == after

def test_stack_queue():
    s = stacks_queues.Stack_Queue()
    assert s.is_empty() == True
    assert s.size() == 0
    s.enqueue(1)
    assert s.dequeue() == 1
    assert s.size() == 0
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    assert s.size() == 3
    assert s.is_empty() == False
    assert s.dequeue() == 1
    assert s.dequeue() == 2
    assert s.dequeue() == 3
    assert s.is_empty() == True
    s.enqueue(1)
    s.enqueue(2)
    assert s.dequeue() == 1
    s.enqueue(3)
    assert s.dequeue() == 2
    assert s.is_empty() == False
    
