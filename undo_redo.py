"""
"action" object
    has "inverse" method, returns new action
"apply" function
    Takes an action and applies it

How can you track state needed to handle undo/redo

Ideas:
    State object
    -2 stacks of actions: undo and redo
    -Redo: when action is "inverted", it gets added to stack
    -Undo: when action is "applied", it gets added to this stack
    -When calling undo, it pops top action and adds to "redo" stack
    -When calling redo, it pops
"""

"""
List of computer science courses: ["Algos","OS","Graphics","ML","Compilers","Arch","Distributed Systems"] 
Pre-reqs for each course: [(5,6),(0,4),(1,2),(1,6),(0,1),(4,1),(3,2)] #e.g. Arch required before DS

Know what order to take course, so you fulfill all pre-reqs.

Write a function that takes these lists and returns for each course, how many pre-reqs it has.
"""

def course_prereqs(course_list, prereq_list):
    course_count = [0]*len(course_list)
    for _, course in prereq_list:
        course_count[course] += 1
    for i, course in enumerate(course_list):
        print(course,' has ', course_count[i],' prereqs.')

"""
For each prereq course, which courses depend on that prereq course?

Ideas:
-Create dict with values as list
-append course to list of dict with key for each course
"""

def course_dependencies(course_list, prereq_list):
    course_dict = {i : [] for i in range(0,len(course_list))}
    for prereq, course in prereq_list:
        course_dict[prereq].append(course)
    print(course_dict)

"""
Key idea: use queue structure to keep track of courses we can take

Questions:
1) Which course can we take right away?
    Find which course has zero prereqs.
    Add any courses meeting these to a queue.
    Once we take course, we can dequeue it and add to order of courses taken
    Then we can decrement number of prereqs for courses that depend upon it.
    Then can add any courses wiht zero remaining preqreqs to queue

Topological sort: given some dependencies, how to do your find an order to complete list of things
    Parallels this example

Challenge: how do you detect when invalid list of prereqs is passed (circular dependencies).
"""