#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Find most common character in a string
# --------------------------------------------------------------
def mostCommon(S) :
    '''
    Assume that S is a nonempty string.
    Return the most common character in the string, 
    but if there is a tie for most common, then 
    Return the alphabetically lowest among the most-common letters.

    FOR THIS QUESTION YOU MUST USE A DICTIONARY.

    For example,
    mostCommon('zabcdefg') returns 'a'
    mostCommon('abcdefeg') returns 'e'
    mostCommon('abcdefega') returns 'a'
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mostComDict = {}

    for c in S:
        if c not in mostComDict.keys():
            mostComDict[c] = 1
        else:
            mostComDict[c] += 1
    
    largestValues = [letter for letter in mostComDict if mostComDict[letter] == max(mostComDict.values())]
    
    if len(largestValues) > 1:
        for a in alphabet:
            if a in largestValues:
                return a

    return largestValues[0]
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(mostCommon('yes'), 'e')
    def test2(self):
        self.assertEqual(mostCommon('(hello)'), 'l')
    def test3(self):
        self.assertEqual(mostCommon('((q))abc(d(r)ef(s))g((t))'),'(')
    def test4(self):
        self.assertEqual(mostCommon('yyeessir'), 'e')
    def test5(self):
        self.assertEqual(mostCommon('yyeess'), 'e')
    def test6(self):
        self.assertEqual(mostCommon('y'), 'y')

if __name__=='__main__':
    unittest.main(exit=True)