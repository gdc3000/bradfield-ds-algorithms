"""
Trade-offs between linear probing and chaining.

Cache-locality:
    TLU -> memory -> Disk
"""

"""
Problem: Building a search engine. One of the components aggregates results from lots of different sorted_iterators.

sorted_iterator {
    hasNext()   bool
    next()  int
}

Given lots of sorted iterators. Aggregating results from 100 sources.

Goal: Return lowest 100 iterators globally

Naive solution:
 -Take first 100 items from all sorted_iterators
 -Add to single list
 -Sort list

Better solution:
  -Take first 100 items from first y iterators
  -Load these into a max heap
  -For next item, if it's less than max, replace max with it and reshuffle
  -Keep going across all iterators
  -When get to a next() in iterator that is larger than max, you can stop looking at that iterator
"""

def find_smallest_100(iter_list):
    max_heap = [None]*100
    for iter in iter_list:
        while iter.hasNext() and iter.next() < max_heap[0]:
            add_to_heap(iter.next()) #add value and iterator
    
    return max_heap

"""
Another approach: 
  -Min heap
  -Get lowest from all of the iters
"""