"""
Goal: Cultivating the problem solving process

Course structure:
   1) Pre-work: Do and send (not optional). Send directly to Elliot.
   2) Live practice in the session. Reserve the right to call by name.
   3) Post-work: optional (do at own pace, maybe months after course)

"Problem-solving is not a spectator sport. Need to put in a lot of practice."

Warm-up problem
-Historian
-Someone handed you lots stack of documents with roman numerals
-Only moves forward XVII (17). E.g. IX (9)not going to happen. Would be VIIII instead.
-Symbols:
    -M 1000
    -D 500
    -C 100
    -L 50
    -X 10
    -V 5
    -I 1

Edge cases:
-Lower case input -> assume not
-Could be out of order or invalid -> assume not
-Should I throw an exception if an invalid roman numeral is passed? - Yes
-Program passed single string? -> assume it is

Approach:
-Check if it is a valid roman numeral
-Parse string letter by letter. Use dictionary to store values of each letter. 
Lookup value in dictionary and add to counter. Return counter when done parsing
input phrase.
"""

def convert_roman_numeral(numeral):
    total = 0
    numeral_dict = {
        'M':1000,
        'D':500,
        'C':100,
        'L':50,
        'X':10,
        'V':5,
        'I':1
    }
    for letter in numeral:
        if letter in numeral_dict:
            total += numeral_dict[letter]
    return total

"""
Reflection: Thoughts on process:
-Write conditions
  -Assumptions
  -Data needed
-Consider data structures that could help
-Speak to someone ("rubber duck")
-Think about test cases
-Write all the edge cases that I think of
-Start by thinking about small examples (reduce problems)
-Think about related problems that you've solved before
    -"more problems you do, the better you'll be"
-Think of different ways to solve every problem
    -"Any problem has a bunch of solutions... it frees you... you don't have to find magic
      password that interviewer has in mind."
    -Try pushing yourself to find a very different approach, rather than tweaking approach
    -First solution is almost always not optimized
-Polya's comment: "all people, including brilliant mathematiciains go through this process"... all problem-solving is bumbling

Other solutions where similar to mine.
"""

"""
Next problem: society has new rule there can be subtractive pairs.
    E.g. IX, represents 9

    If a smaller number comes before a larger number, then treat it as "subtractive pair"
        E.g. I < X, so treat I as subtraction
        Unless TWO NUMBERS handle as subtractive pair
    Otherwise, numbers must go bigger to smaller. 

    Not all pairs are allowed. Precisely:
        -I can preceede V or X
        -X can precede L, C
        -C can precede D or M.

    Can assume that given roman numerals are valid.

Approach:
    -assume valid roman numeral is passed
    -initialize counter
    -initialize dictionaries needed
    -loop through string letter by letter:
        -if not on last letter, check if given letter is less than next letter
        -if true:
           -make sure next letter is in list of valid letters. Create a dictionary where
            the valid next letters are associated with each letter. Throw an exception if
            either key is not in this dictionary or if next letter is not valid.
           -subtract current letter
        -if false:
           -add current letter

Questions I would ask:
"""
def convert_roman_numeral_2(numeral):
    total = 0
    numeral_dict = {
        'M':1000,
        'D':500,
        'C':100,
        'L':50,
        'X':10,
        'V':5,
        'I':1
    }
    valid_next_letter = {
        'I':['V','X'],
        'X':['L','C'],
        'C':['D','M']
    }
    for i, letter in enumerate(numeral):
        if i == len(numeral) - 1:
            total += numeral_dict[letter]
        else:
            next_letter = numeral[i+1]
            if numeral_dict[letter] < numeral_dict[next_letter]:
                assert next_letter in valid_next_letter[letter]
                total -= numeral_dict[letter]
            else:
                total += numeral_dict[letter]
    return total

"""
Reflection:
-Important to worry about boundary condition since checking both next letter and current letter
-Two solutions: Grouping into two versus look ahead.
-Recursive ideas?
-Check with "slicer" to handle edge case in Python (e.g. string[i+1:i+2])
-Another idea:
    -List with tuples with valid pairs
        -Include both 1-letter (X) and 2-letter (XC) numerals in list
    -One outer loop goes through all numerals
    -Peel off numerals in order that match (s.startswith)
    -Add value to result
    -User slicer to increment list s = s[len(numeral):]
    -Return value
"""
def convert_roman_numeral_3(numeral):
    total = 0
    s=numeral
    numeral_list = [
        ('M',1000),
        ('CM',900),
        ('D',500),
        ('CD',400),
        ('C',100),
        ('XC',90),
        ('L',50),
        ('XL',40),
        ('X',10),
        ('IX',9),
        ('V',5),
        ('IV',4),
        ('I',1)
    ]
    for i in numeral_list:
        num, val = i
        while s.startswith(num):
            total += val
            s = s[len(num):]
    return total


"""
Challenge problem: Let's say that given numeral. Convert shortest possible.
    e.g. IIIII -> V

Problem: Given a roman numeral, shorten it.

Edge cases:
    -What if you get passed more than two values in a row that are lower than the next one.
      -> Assume this won't happen
    -Assume input can't be greater than 3000

Approach:
    -Define list of values for all roman numerals and subtracted pairs (1000 to 1)
    -Accept input "long" roman numeral
    -For each roman numeral in the list, count the number appearing in the input (starting with the
     highest letter). If there are more than 4+ occurences of this letter and it is I,X,C or M, then 
     replace it with the next largest number up. If there are more than 2+ occurence of other numbers, 
     then replace it with the next letter up the numeral list.
        -Edge case: If you encounter two "subtracted pairs" in a row, this won't work.
    -

"""
import math
def short_roman_numeral(numeral):
    numeral_list = [
        ('M',1000),
        ('CM',900),
        ('D',500),
        ('CD',400),
        ('C',100),
        ('XC',90),
        ('L',50),
        ('XL',40),
        ('X',10),
        ('IX',9),
        ('V',5),
        ('IV',4),
        ('I',1)
    ]
    output = ''
    numeral_count = len(numeral_list)-1

    #iterate through whole range
    for i in range(numeral_count, 0, -4):
        #count total value of symbols in group
        val_sum = 0
        for j in range(i, i-4, -1):
            sym, val = numeral_list[j]
            sym_length = len(sym)
            while numeral.endswith(sym):
                numeral = numeral[:-sym_length]
                val_sum += val

        #bump any amount over ten up to the next tier, append to end of numeral
        ten_sym, ten_val = numeral_list[i-4]
        ten_count = val_sum // ten_val
        val_sum = val_sum % ten_val
        numeral = numeral + ten_count * ten_sym
        
        #append write combo of symbols to output for remaining val_sum
        append = ''
        for j in range(i-3,i+1,1):
            sym, val = numeral_list[j]
            append_count = val_sum // val
            val_sum = val_sum % val
            append += sym * append_count
        
        output = append + output

    #append Ms to output
    sym, val = numeral_list[0]
    sym_length = len(sym)
    while numeral.endswith(sym):
        numeral = numeral[:-sym_length]
        output = sym + output

    return output
    
assert short_roman_numeral('MDLXIIIII') == 'MDLXV'
assert short_roman_numeral('MDLXIIII') == 'MDLXIV'
assert short_roman_numeral('MDLXIIIIIIIII') == 'MDLXIX'
assert short_roman_numeral('MDLXXXXXIIIIIIIII') == 'MDCIX'
assert short_roman_numeral('MDLXXXXXIVIV') == 'MDCVIII'
assert short_roman_numeral('MCMDDDD') == 'MMMCM'
assert short_roman_numeral('MCMDDDDIVIV') == 'MMMCMVIII'