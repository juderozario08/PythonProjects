import unittest
from math import sqrt
"""
2D arrays

Convert a dictionary into 2D Array

convert_dict_array(dictionary) :
..gives a dictionary, where the keys are the coordinates of a 2D array,
and their associated value is the element at these coordinates in the 2D array.

Assume the array is square, i.e., number of rows = number of columns,
and that the dictionary specifies every element of the matrix.

Reconstruct and return the 2D array associated with the dictionary. 

Hint: to find the size of the array, compute the square root of something

Example 1:
A = {(0,0): 0, (0,1): 1, (1, 0):2, (1,1):3}
result = [[0, 1], [2, 3]]
  
Example 2:
A = {(0,0): 60, (0,1): 40, (0,2): 18, (1, 0):40, (1,1):23, (1,2):17, (2, 0):14, (2,1):12, (2,2):22}
result = [[60, 40, 18], [40, 23, 17], [14, 12, 22]]

Example 3:
A = {(0,0): 60, (0,1): 40, (1,0):23, (1,1):14}
result = [[60, 40], [23, 14]]

"""
# --------------------------------------------------------------
# Your implementation: 
# --------------------------------------------------------------
def convert_dict_array(dictionary) :
    # YOUR CODE GOES HERE
    size = int(sqrt(len(dictionary)))
    L = []

    for m in range(size):
        sublist = []
        for n in range(size):
            sublist.append(0)
        L.append(sublist)

    for key, value in dictionary.items():
        L[key[0]][key[1]] = value
    return L

    pass

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
  def test1(self):
    self.assertEqual(convert_dict_array({(0,0): 0, (0,1): 1, (1, 0):2, (1,1):3}),  [[0, 1], [2, 3]])
  def test2(self):
    self.assertEqual(convert_dict_array({(0,0): 60, (0,1): 40, (0,2): 18, (1, 0):40, (1,1):23, (1,2):17, (2, 0):14, (2,1):12, (2,2):22}), [[60, 40, 18], [40, 23, 17], [14, 12, 22]])
  def test3(self):
    self.assertEqual(convert_dict_array({(0,0): 60, (0,1): 40, (1,0):23, (1,1):14}), [[60, 40], [23, 14]])
  def test4(self):
    self.assertEqual(convert_dict_array({}), [])

         
if __name__ == '__main__':
  unittest.main(exit=True)
 
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
