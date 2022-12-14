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