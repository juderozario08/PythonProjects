import unittest

# the fibonacci numbers are a sequence in which each number is the sum of the two preceding ones
# i.e. 1, 1, 2, 3, 5, 8, 13, 21...
# write a function fibonacci(n) that returns the nth element in the fibonacci sequence
# you must use recursion to solve this problem

# --------------------------------------------------------------
# YOUR ANSWER HERE
# --------------------------------------------------------------

def fibonacci(n):
    # your code here
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# --------------------------------------------------------------
# Test Cases
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(fibonacci(0), 0)

    def test2(self):
        self.assertEqual(fibonacci(1), 1)

    def test3(self):
        self.assertEqual(fibonacci(2), 1)

    def test3(self):
        self.assertEqual(fibonacci(6), 8)

    def test4(self):
        self.assertEqual(fibonacci(9), 34)

if __name__ == '__main__':
    unittest.main(exit=True)