#!/usr/bin/python3
import unittest


def func3(lis):
    '''
    Assume lis is a list of integers and characters.
    Return (cha, i) where cha is the last character in the list 
    and i is the index of the last character.
    Note 1: you may use isinstance(d, int) or isinstance(d, str) 
    to check the type of d.
    Note 2: index i should be nonnegative (do not use negtive index)

    For example, lis = ['e', 'f', 2, 3] should return ('f', 1)
    '''
    # YOUR CODE GOES HERE
    indexchar = None

    for i in range(len(lis)-1,0,-1):
        if type(lis[i]) == str:
            indexchar = i
            break
    return (lis[indexchar],indexchar)

    pass


# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(func3([1, 2, 3, 'a', 'b', 'c']), ('c', 5))

    def test2(self):
        self.assertEqual(func3(['f', 'b', 'c', 1, 2, 3]), ('c', 2))

    def test3(self):
        self.assertEqual(func3([3, 2, 'b', 'b', 'e', 3]), ('e', 4))

    def test4(self):
        self.assertEqual(func3([3, 2, 5, 3, 'c', 'b']), ('b', 5))

    def test5(self):
        self.assertEqual(func3([3, 2, 1, 'd']), ('d', 3))


if __name__ == '__main__':
    unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
