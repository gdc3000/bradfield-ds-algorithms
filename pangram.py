"""
Polya's Approach: https://math.berkeley.edu/~gmelvin/polya.pdf
Problem: Write a function that returns true if a given phrase is a pangram (contains every letter at least once)

Edge cases:
  1. Lower case and upper case characters - we'll assume our solution is case insensitive
  2. Special characters - we'll only consider standard letters

Here's an approach that might work:
  a. Create a list with 26 elements, all set to False. Traverse the letters in a given phrase. 
     Update the element corresponding with a given letter to true when you encounter it. All letters encountered 
     should be converted to lower case. After traversing the phrase, return True if all elements in the list 
     are true and false otherwise.
"""

def check_if_pangram_a(phrase):
   letter_check = [False for i in range(0,26)]
   for char in phrase:
      char_index = ord(char.lower()) - 97
      if char_index <= 25 and char_index >= 0:
         letter_check[char_index] = True
   return all(letter_check)

"""
Reflection:
   1. If the given phrase doesn't contain at least 26 characters, then it definitely isn't a pangram. Check the len of the
      the phrase and return False if it's less than 26 characters long.
   2. It might be easier to use a dictionary with all of the letters versus a list where you have to convert each letter to
      the approach element number when updating the list.

Another approach:
  b. Similar to (a), but instead of a list keep a dictionary with 26 keys (one for each letter). Everytime
     you encounter a letter in your phrase, update the counter in the dictionary for that letter. After
     traversing the phrase, check that each counter is greater than or equal to 1 and return true if is, false 
     otherwise. We'll also add a checker to see if the phrase is at least 26 characters long.
"""
def check_if_pangram_b(phrase):
   if _phrase_too_short(phrase):
      return False

   letter_check = {chr(i+97):0 for i in range(0,26)}
   for char in phrase:
      l_char = char.lower()
      if l_char in letter_check:
         letter_check[l_char] += 1
   return all(value > 0 for value in letter_check.values())

def _phrase_too_short(phrase):
   return len(phrase) < 26

"""
Reflection:
   3. Both a and b require you traverse the entire list which may not be needed. For a above, you might be able to keep 
      a counter that updates each time a unique letter is encountered. Once it hits 26, you can return true automatically
      without finishing your traversal of the phrase.

Another approach:
  c. Almost the opposite of b: you could start with a set of all of letters and remove each letter once you encounter it.
     You return True once the set is empty or False if you finish parsing the phrase with a non-empty set left.
"""
def check_if_pangram_c(phrase):
   if _phrase_too_short(phrase):
      return False
      
   letter_set = set([chr(i+97) for i in range(0,26)])
   print(letter_set)
   for char in phrase:
      l_char = char.lower()
      if l_char in letter_set: 
         letter_set.remove(l_char)
      if not letter_set:
         return True
   return False
"""
Reflection:
   4. All of the above approaches run in O(nlogn) worst case, since we traverse the list and then lookup values
      from a set, dictionary or list. 
   5. It might be possible to improve space and time efficiency using bitwise operators.
"""