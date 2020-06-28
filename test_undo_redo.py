import undo_redo

courses = ["Algos","OS","Graphics","ML","Compilers","Arch","Distributed Systems"] 
prereqs = [(5,6),(0,4),(1,2),(1,6),(0,1),(4,1),(3,2)]

def test_course_prereqs():
    undo_redo.course_prereqs(courses, prereqs)
    assert True

def test_course_prereqs():
    undo_redo.course_dependencies(courses, prereqs)
    assert False