#!/usr/bin/python3
import unittest


def func1(lis):
    '''
    Assume lis is a list of integers and characters.
    Return (cha, i) where cha is the first character in the list 
    and i is the index of the first character.
    Note 1: you may use isinstance(d, int) or 
    isinstance(d, str) to check the type of d
    Note 2: index i should be nonnegative (do not use negtive index)

    For example, lis = ['e', 'f', 2] should return ('e', 0)
    lis = [3, 5, 'f', 'g', 2] should return ('f', 2)
    '''
    # YOUR CODE GOES HERE
    for i in range(len(lis)):
        if isinstance(lis[i], str):
            cha = lis[i]
            return(cha, i)


# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(func1([1, 2, 3, 'a', 'b', 'c']), ('a', 3))

    def test2(self):
        self.assertEqual(func1(['f', 'b', 'c', 1, 2, 3]), ('f', 0))

    def test3(self):
        self.assertEqual(func1([3, 2, 'b', 'b', 'c', 3]), ('b', 2))

    def test4(self):
        self.assertEqual(func1([3, 2, 5, 3, 'c', 'b']), ('c', 4))

    def test5(self):
        self.assertEqual(func1([3, 2, 1, 'd']), ('d', 3))


if __name__ == '__main__':
    unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
