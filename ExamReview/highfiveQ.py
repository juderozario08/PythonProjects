
import unittest

def highfive_recursive(n):
    '''
    In a party of n people, each person will high five 
    another person only once.  

    Write a RECURSIVE function to compute and return
    the total number of high fives. 
    Assume that if n is less than or equal to 1 the 
    function should return 0.

    For example, if there are 3 people (i.e. A, B, C), 
    then there are 3 high-fives (as AB, AC, BC),
    so highfive_recursive(3) returns 3.
    '''
# --------------------------------------------------------------
# YOUR ANSWER HERE
# --------------------------------------------------------------

    # YOUR CODE GOES HERE

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------

class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(highfive_recursive(5), 10)

    def test2(self):
        self.assertEqual(highfive_recursive(2), 1)
        
    def test3(self):
        self.assertEqual(highfive_recursive(-1), 0)
        
    def test4(self):
        self.assertEqual(highfive_recursive(1), 0)
        
    def test5(self):
        self.assertEqual(highfive_recursive(100), 4950)
        
if __name__ == '__main__':
    unittest.main(exit=True)
    
from bdb import Bdb
import sys

class RecursionDetected(Exception):
    pass

class RecursionDetector(Bdb):
    def do_clear(self, arg):
        pass

    def __init__(self, *args):
        Bdb.__init__(self, *args)
        self.stack = set()

    def user_call(self, frame, argument_list):
        code = frame.f_code
        if code in self.stack:
            raise RecursionDetected
        self.stack.add(code)

    def user_return(self, frame, return_value):
        self.stack.remove(frame.f_code)

def test_recursion(func):
    detector = RecursionDetector()
    detector.set_trace()
    try:
        func()
    except RecursionDetected:
        return True
    else:
        return False
    finally:
        sys.settrace(None)

assert test_recursion(lambda: highfive_recursive(5))
assert test_recursion(lambda: highfive_recursive(3))
assert not test_recursion(lambda: highfive_recursive(2))
assert not test_recursion(lambda: highfive_recursive(1))
assert not test_recursion(lambda: highfive_recursive(-1))
assert highfive_recursive(5) == 10
assert highfive_recursive(3) == 3
assert highfive_recursive(2) == 1
assert highfive_recursive(1) == 0
assert highfive_recursive(-1) == 0
assert not test_recursion(lambda: highfive_iterative(5))
assert not test_recursion(lambda: map(highfive_iterative, range(5)))
assert highfive_iterative(5) == highfive_recursive(5) == 10
