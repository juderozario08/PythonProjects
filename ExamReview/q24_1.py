
import unittest

def handshake_recursive(n):
    '''
    In a party of n people, each person will shake her/his hand 
    with each other person only once.  

    Write a RECURSIVE function to compute and return
    the total number of hand-shakes. 
    Assume that if n is less than or equal to 1 the 
    function should return 0.

    For example, if there are 3 people (i.e. A, B, C), 
    then there are 3 hand-shakes (as AB, AC, BC),
    so handshake_recursive(3) returns 3.

    Note 0: a nonrecursive solution is worth ZERO.
    Note 1: you are NOT allowed to change the function name, 
    and NOT allowed to change the testing part. Otherwise the mark is ZERO.
    Note 3: respect the boundaries given by the test cases.
    '''
    # YOUR CODE GOES HERE
    if n <= 1:
        return 0
    else:
        return n-1 + handshake_recursive(n-1)

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------

class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(handshake_recursive(5), 10)

    def test2(self):
        self.assertEqual(handshake_recursive(2), 1)
        
    def test3(self):
        self.assertEqual(handshake_recursive(-1), 0)
        
    def test4(self):
        self.assertEqual(handshake_recursive(1), 0)
        
    def test5(self):
        self.assertEqual(handshake_recursive(100), 4950)
        
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

assert test_recursion(lambda: handshake_recursive(5))
assert test_recursion(lambda: handshake_recursive(3))
assert not test_recursion(lambda: handshake_recursive(2))
assert not test_recursion(lambda: handshake_recursive(1))
assert not test_recursion(lambda: handshake_recursive(-1))
assert handshake_recursive(5) == 10
assert handshake_recursive(3) == 3
assert handshake_recursive(2) == 1
assert handshake_recursive(1) == 0
assert handshake_recursive(-1) == 0
assert not test_recursion(lambda: handshake_iterative(5))
assert not test_recursion(lambda: map(handshake_iterative, range(5)))
assert handshake_iterative(5) == handshake_recursive(5) == 10
