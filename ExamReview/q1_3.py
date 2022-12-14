#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Blood sugar chart when fasting
# (Caveat: just an excercise, not necessarily true)
# --------------------------------------------------------------
def fastingbloodsugar(mgdl, diabetes) :
    '''
    Assume that mgdl is a number representing mg of sugar per dl of blood,
    and diabetes is True or False.
    Returns 'Recommended' 
    when diabetes is False and mgdl is 70 to 99, inclusive,
    or when diabetes is True and mgdl is 80 to 130, inclusive
    otherwise, returns 'Concerned'.

    For example, 
    fastingbloodsugar(80, False) returns Recommended
    fastingbloodsugar(80, True) returns Recommended
    fastingbloodsugar(100, True) returns Recommended
    fastingbloodsugar(100, False) returns Concerned
    '''
    if diabetes:
      if mgdl >= 80 and mgdl <= 130:
        return 'Recommended'
    else:
      if mgdl >= 70 and mgdl <= 99:
        return 'Recommended'
    return 'Concerned'

    pass
    
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(fastingbloodsugar(77, False), 'Recommended')
 def test2(self):
  self.assertEqual(fastingbloodsugar(77, True), 'Concerned')
 def test3(self):
  self.assertEqual(fastingbloodsugar(131, True), 'Concerned')
 def test4(self):
  self.assertEqual(fastingbloodsugar(99.2, False), 'Concerned')
 def test5(self):
  self.assertEqual(fastingbloodsugar(99, False), 'Recommended')
 def test6(self):
  self.assertEqual(fastingbloodsugar(80, True), 'Recommended')


if __name__ == '__main__':
 unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------

