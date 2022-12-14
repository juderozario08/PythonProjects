import unittest
import Exam_Module

'''
You must do blackbox testing on a function find_furthest, which can
be found in the Exam_Module file, imported above. You do
not have access to this module.

This function takes one argument, Letters, an unsorted list of letters.
You can assume that the letters in Letters are all different from each other.
The function returns the index of the maximum letter in Letters.
For example, if Letters is ['d', 'a', 'f', 'b'] then find_furthest(Letters)
would return 2, since 'f' is the largest letter and has index 2.
If the list Letters is empty, then return None.

You are to write FOUR unit tests. At least two should account
for edge cases (abnormal cases). Recall that to use a function
from a different file, the syntax is filename.function_name(arguments).

A first test case is given to you as an example below.

You do not need to know what happens inside of the find_furthest function
to test it. You simply need to know what it returns, which is stated
above.
'''

class AlphaTest(unittest.TestCase):
    def test1(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.find_furthest(['c', 'b', 'a'])
        b = 0
        self.assertEqual(a, b)
    def test2(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.find_furthest(['z','b','d','r'])
        b = 0
        self.assertEqual(a, b)
    def test3(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.find_furthest([])
        b = None
        self.assertEqual(a, b)
    def test4(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.find_furthest(['b','bb','bbb','b'])
        b = 2
        self.assertEqual(a, b)
    def test5(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.find_furthest(['ac','by',' ','za'])
        b = 3
        self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main(exit=True)
