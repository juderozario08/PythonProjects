import unittest

# x and epsilon are floating point numbers. epsilon is the difference in error your answer can be. Assume epsilon > 0
# write a function find_root(x, epsilon) that uses bisection search to find the square root of x such that

# While y**2 is within the epsilon of x
# If y**2 > x: Update the higher bound to be y
# Else: Update the lower bound to be y

# Note: You must use bisection search to implement the function. Name your function find_root

# --------------------------------------------------------------
# YOUR ANSWER HERE
# --------------------------------------------------------------

# --------------------------------------------------------------
# Test Cases
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        x = 125
        epsilon = 0.01
        error = find_root(x, epsilon)**2 - x
        self.assertTrue(error < epsilon)

    def test2(self):
        x = 0
        epsilon = 0.001
        error = find_root(x, epsilon)**2 - x
        self.assertTrue(error < epsilon)
    
    def test3(self):
        x = 3213123
        epsilon = 0.001
        error = find_root(x, epsilon)**2 - x
        self.assertTrue(error < epsilon)

if __name__ == '__main__':
    unittest.main(exit=True)