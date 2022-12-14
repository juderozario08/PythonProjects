

#QUESTION 6 - q1_5.py
#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Jump to the ground.
# --------------------------------------------------------------
def jump(n):
    '''
    Assumes that n is an integer greater than or equal to zero.
    Returns half of n if n is even, except when n is a multiple of 7,
    in which case it returns 0, and 
    returns 3 times n plus 1 if n is odd, 
    except when n is a multiple of 7,
    in which case it returns 0.

    For example, 
    jump(4) returns 2
    jump(5) returns 16 
    jump(7) returns 0
    jump(14) returns 0
    '''

    if n%7 == 0:
      return 0
    
    elif n%2 == 0:
      return n/2
    
    elif n%2 != 0:
      return n*3+1

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(jump(3), 10)
 def test2(self):
  self.assertEqual(jump(5), 16)
 def test3(self):
  self.assertEqual(jump(10), 5)
 def test4(self):
  self.assertEqual(jump(0), 0)
 def test5(self):
  self.assertEqual(jump(21), 0)
 def test6(self):
  self.assertEqual(jump(28), 0)

if __name__ == '__main__':
 unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

#QUESTION 7 - q2_2.py
#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Flip case.
# --------------------------------------------------------------
def under(sentence):
    '''
    Assumes sentence is a string.
    Returns a string copy of string except that an underscore is added
    after each character which is not a blank and not an underscore.

    For example, 
    under('This rainy day.') returns 'T_h_i_s_ r_a_i_n_y_ d_a_y_._'  
    under('This _blue_ day.') return 'T_h_i_s_ _b_l_u_e__ d_a_y_._'  
    '''
    underSentence = ""
    for c in sentence:
      underSentence += c

      if c != '_' and c != ' ':
        underSentence += '_'
    
    return underSentence

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(under('blue'), 'b_l_u_e_')
 def test2(self):
  self.assertEqual(under('This rainy day.'), 'T_h_i_s_ r_a_i_n_y_ d_a_y_._')
 def test3(self):
  self.assertEqual(under('a'), 'a_')
 def test4(self):
  self.assertEqual(under('_red_, green, blue'), '_r_e_d__,_ g_r_e_e_n_,_ b_l_u_e_')
 def test5(self):
  self.assertEqual(under('_ _ _'), '_ _ _')
  


if __name__ == '__main__':
 unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

#QUESTION 8 - q4_7.py
#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Underscores
# --------------------------------------------------------------
def underscore(sentence):
    '''
    Assumes sentence is a string of words separated by blanks,
    and that sentence is not an empty string.
    Returns a string just like sentence but that there is an 
    underscore after each letter in each word except the last letter of 
    each word.
    
    For example, 
    underscore('This is a rainy day') returns 'T_h_i_s i_s a r_a_i_n_y d_a_y'  
    underscore('blue') produces 'b_l_u_e'.

    '''

    underSentence = ''

    for c in range(len(sentence)-1):
      underSentence += sentence[c]

      if sentence[c] != ' ' and sentence[c+1] != ' ':
        underSentence += '_'
    
    return underSentence + sentence[-1]

    pass
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(underscore('blue'), 'b_l_u_e')
 def test2(self):
  self.assertEqual(underscore('This is a rainy day'), 'T_h_i_s i_s a r_a_i_n_y d_a_y')
 def test3(self):
  self.assertEqual(underscore('a'), 'a')
 def test4(self):
  self.assertEqual(underscore('Sugar Plum 5!'), 'S_u_g_a_r P_l_u_m 5_!')

if __name__ == '__main__':
 unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

#QUESTION 9 - q6_1.py
#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Find most common character in a string
# --------------------------------------------------------------
def mostCommon(S) :
    '''
    Assume that S is a nonempty string.
    Return the most common character in the string, 
    but if there is a tie for most common, then 
    Return the alphabetically lowest among the most-common letters.

    FOR THIS QUESTION YOU MUST USE A DICTIONARY.

    For example,
    mostCommon('zabcdefg') returns 'a'
    mostCommon('abcdefeg') returns 'e'
    mostCommon('abcdefega') returns 'a'
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mostComDict = {}

    for c in S:
        if c not in mostComDict.keys():
            mostComDict[c] = 1
        else:
            mostComDict[c] += 1
    
    largestValues = [letter for letter in mostComDict if mostComDict[letter] == max(mostComDict.values())]
    
    if len(largestValues) > 1:
        for a in alphabet:
            if a in largestValues:
                return a

    return largestValues[0]
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(mostCommon('yes'), 'e')
    def test2(self):
        self.assertEqual(mostCommon('(hello)'), 'l')
    def test3(self):
        self.assertEqual(mostCommon('((q))abc(d(r)ef(s))g((t))'),'(')
    def test4(self):
        self.assertEqual(mostCommon('yyeessir'), 'e')
    def test5(self):
        self.assertEqual(mostCommon('yyeess'), 'e')
    def test6(self):
        self.assertEqual(mostCommon('y'), 'y')

if __name__=='__main__':
    unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

#QUESTION 10 - q7_11.py
#!/usr/bin/python3
import unittest
def recursiveCount(l) :
    '''
    Assumes l is a value or a list of values and lists (of values and lists of ...).
    Returns the number of values/lists

    You must use RECURSION to solve the problem.

    For example, 
    recursiveCount(5) is 1
    recursiveCount([1,[[[[2]]]]]) is 7

	Note that type([1])==list
    '''

    numberOfVL = 1
    if type(l) == list:
        for element in l:
            if type(element) == list:
                numberOfVL+=recursiveCount(element)
            else:
                numberOfVL+=1
    else:
        return 1

    return numberOfVL
# --------------------------------------------------------------
# TEST CASES
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(recursiveCount([1,2,3]),4)
    def test2(self):
        self.assertEqual(recursiveCount([[1,[2],[[]]],3,[4]]),10)
    def test3(self):
        self.assertEqual(recursiveCount(5),1)
    def test4(self):
        self.assertEqual(recursiveCount([[[[]]]]),4)
    def test5(self):
        self.assertEqual(recursiveCount([1,[[[[2]]]]]),7)

if __name__=='__main__':
    unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

#QUESTION 11 q8_6.py
#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# 2D array
# --------------------------------------------------------------
def biggestRange(matrix) :
  '''
  Assume that matrix is a two-dimensional rectangular matrix of integers.
  Return the index of the column with the biggest range of numbers, 
  where range is calculated as the maximum minus the minimum number in the column.

  For example, in the following matrix the first column has range 1 to 20,
  the second column has range 2 to 10, and the third column has range 3 to
  38.  Taking the differences for the size of the ranges: 19, 8, 35, so 
  column 2 (the third column)  has the largest range, 
  and the function would return 2.
  [[5, 2, 38],\
    [1, 2, 20],\
    [3, 10, 3],\
    [20, 8, 9],\
    [8, 10, 5]]
  If there is a tie, return the lowest column number of the tie.
  Hint: it might help to convert a column to a simple list so that you can 
  use the min and max functions.
  '''

  transposedMatrix = []
  temp = []

  for i in range (len(matrix[0])):
    for j in range (len(matrix)):
      temp.append(matrix[j][i])

      if len(temp) == len(matrix):
        transposedMatrix.append(temp)
        temp = []

  largestColumn = 0
  largestRange = max(transposedMatrix[0]) - min(transposedMatrix[0])

  for c in range (len(transposedMatrix)):
    currentRange = max(transposedMatrix[c]) - min(transposedMatrix[c])

    if currentRange > largestRange:
      largestColumn = c
      largestRange = currentRange

  return largestColumn

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(biggestRange([[5, 2, 38], [1, 2, 20], [3, 10, 3], [20, 8, 9], [8, 10, 5]]), 2)
 def test2(self):
  self.assertEqual(biggestRange([[-5, -1, -2], [-1, -1, -20], [-3, -10, -3], [-8, -10, -9]]), 2)
 def test3(self):
  self.assertEqual(biggestRange([[-5, -1, -2]]), 0)
 def test4(self):
  self.assertEqual(biggestRange([[3, 9, 1, 1, 2], [2, 1, 1, 9, 3]]), 1)


if __name__ == '__main__':
  unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------