#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Grades in Letters.
# --------------------------------------------------------------
def letterGrade(score):
    '''
    Assume that score is a floating point number from 0.0 to 100.0, inclusive.
    Convert a numerical grade to a letter grade, 'A', 'B', 'C', 'D' or 'F', 
    where the cutoffs for 'A', 'B', 'C', 'D' are 90, 80, 70, and 60 
    respectively. So 'F' will be below 60.
    Returns the letter grade corresponding to the score.

    For example, 90 to 100 inclusive is 'A',
    'B' is less than 90, but at least 80, 
    and so on.
    '''
    if score < 60:
      return("F")
    elif score >= 60 and score<70:
      return("D")
    elif score >= 70 and score<80:
      return("C")
    elif score >= 80 and score<90:
      return("B")
    else:
      return("A")
    
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(letterGrade(77), 'C')
 def test2(self):
  self.assertEqual(letterGrade(90), 'A')
 def test3(self):
  self.assertEqual(letterGrade(100), 'A')
 def test4(self):
  self.assertEqual(letterGrade(59), 'F')
 def test5(self):
  self.assertEqual(letterGrade(60), 'D')
 def test6(self):
  self.assertEqual(letterGrade(70), 'C')


if __name__ == '__main__':
 unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

