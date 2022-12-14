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
