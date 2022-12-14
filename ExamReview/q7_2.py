#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Recursion: Finding the number of occurrences of a substring
# --------------------------------------------------------------
def countsubstrings(substring, S) :
    '''
    Assume that substring and S are nonempty strings.
    Return the number of times substring occurs in S.

    CONSTRAINT: YOU MUST USE RECURSION. NO LOOPS. MARK FOR LOOP IS 0.
    CONSTRAINT: YOU CANNOT USE THE STRING FUNCTION COUNT().

    For example,
    countsubstrings('cat', 'catdogcatcat') returns 3
    countsubstrings('horse', 'of course') returns 0
    '''

    if len(substring) > len(S):
      return 0
    else:
      count = 0
      for i in range(len(substring)):
        if substring[i] == S[i]:
          count += 1
      if count == len(substring):
        return 1 + countsubstrings(substring, S[1:])
      else:
        return 0 + countsubstrings(substring, S[1:])

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(countsubstrings('cat', 'catdogcatcat'), 3)
 def test2(self):
  self.assertEqual(countsubstrings('horse', 'of course'), 0)
 def test3(self):
  self.assertEqual(countsubstrings('horse', 'h o r s e'), 0)
 def test4(self):
  self.assertEqual(countsubstrings('111', '111 111 111'), 3)
 def test5(self):
  self.assertEqual(countsubstrings('111', '111111111'), 7)


if __name__ == '__main__':
 unittest.main(exit=True)




# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
