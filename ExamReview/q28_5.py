import unittest
import Exam_Module

'''
You must do blackbox testing on a function count_letters, which can
be found in the Exam_Module file, imported above. You do
not have access to this module.

This function takes one argument, a string, and counts ONLY
the lowercase letters in it. It then returns the number of letters as an int.
If the string contains numbers or non-letter characters, or uppercase letters,
it does not count them.

You are to write FOUR unit tests. At least two should account
for edge cases (abnormal cases). Recall that to use a function
from a different file, the syntax is filename.function_name(arguments).

A test case, test1, is given to you as an example below.

You do not need to know what happens inside of the count_letters function
to test it. You simply need to know what it returns, which is stated
above.
'''

class CountTest(unittest.TestCase):
    def test1(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.count_letters('a123b')
        b = 2
        self.assertEqual(a, b)
        
    def test2(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.count_letters('')
        b = 0
        self.assertEqual(a, b)
        
    def test3(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.count_letters('123')
        b = 0
        self.assertEqual(a, b)

    def test4(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.count_letters('ABab')
        b = 2
        self.assertEqual(a, b)

    def test5(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.count_letters('AB12')
        b = 0
        self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main(exit=True)
