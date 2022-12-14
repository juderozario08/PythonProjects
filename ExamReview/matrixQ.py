import unittest

# Make a function "topToBottom" that given a list with n words all of length n, returns a 2D array with each word reading from top to bottom
#   ex input: [hello, howdy, world, mango, place]
#   ex output: [[h, h, w, m, p],
#               [e, o, o, a, l],
#               [l, w, r, n, a],
#               [l, d, l, g, c],
#               [o, y, d, o, e]]

# --------------------------------------------------------------
# YOUR ANSWER HERE
# --------------------------------------------------------------

# --------------------------------------------------------------
# Test Cases
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(topToBottom(["hello", "howdy", "world", "mango", "place"]), [['h', 'h', 'w', 'm', 'p'], ['e', 'o', 'o', 'a', 'l'], ['l', 'w', 'r', 'n', 'a'], ['l', 'd', 'l', 'g', 'c'], ['o', 'y', 'd', 'o', 'e']])
    def test2(self):
        self.assertEqual(topToBottom(["to", "no"]), [['t', 'n'], ['o', 'o']])
    def test3(self):
        self.assertEqual(topToBottom(["I"]), [['I']])

if __name__ == '__main__':
    unittest.main(exit=True)