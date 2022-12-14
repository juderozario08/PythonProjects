#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# 2D array
# --------------------------------------------------------------
def biggestRange(matrix) :
  '''
  Assume that matrix is a two-dimensional rectangular matrix of integers.
  Return the index of the column with the biggest range of numbers, 
  where range is calculated as the maximum minus the minimum number in the column.

  For example, in the following matrix the first column has range 1 to 20,
  the second column has range 2 to 10, and the third column has range 3 to
  38.  Taking the differences for the size of the ranges: 19, 8, 35, so 
  column 2 (the third column)  has the largest range, 
  and the function would return 2.
  [[5, 2, 38],\
    [1, 2, 20],\
    [3, 10, 3],\
    [20, 8, 9],\
    [8, 10, 5]]
  If there is a tie, return the lowest column number of the tie.
  Hint: it might help to convert a column to a simple list so that you can 
  use the min and max functions.
  '''

  transposedMatrix = []
  temp = []

  for i in range (len(matrix[0])):
    for j in range (len(matrix)):
      temp.append(matrix[j][i])

      if len(temp) == len(matrix):
        transposedMatrix.append(temp)
        temp = []

  largestColumn = 0
  largestRange = max(transposedMatrix[0]) - min(transposedMatrix[0])

  for c in range (len(transposedMatrix)):
    currentRange = max(transposedMatrix[c]) - min(transposedMatrix[c])

    if currentRange > largestRange:
      largestColumn = c
      largestRange = currentRange

  return largestColumn

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(biggestRange([[5, 2, 38], [1, 2, 20], [3, 10, 3], [20, 8, 9], [8, 10, 5]]), 2)
 def test2(self):
  self.assertEqual(biggestRange([[-5, -1, -2], [-1, -1, -20], [-3, -10, -3], [-8, -10, -9]]), 2)
 def test3(self):
  self.assertEqual(biggestRange([[-5, -1, -2]]), 0)
 def test4(self):
  self.assertEqual(biggestRange([[3, 9, 1, 1, 2], [2, 1, 1, 9, 3]]), 1)


if __name__ == '__main__':
  unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
