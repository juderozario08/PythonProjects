#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Underscores
# --------------------------------------------------------------
def underscore(sentence):
    '''
    Assumes sentence is a string of words separated by blanks,
    and that sentence is not an empty string.
    Returns a string just like sentence but that there is an 
    underscore after each letter in each word except the last letter of 
    each word.
    
    For example, 
    underscore('This is a rainy day') returns 'T_h_i_s i_s a r_a_i_n_y d_a_y'  
    underscore('blue') produces 'b_l_u_e'.

    '''

    underSentence = ''

    for c in range(len(sentence)-1):
      underSentence += sentence[c]

      if sentence[c] != ' ' and sentence[c+1] != ' ':
        underSentence += '_'
    
    return underSentence + sentence[-1]

    pass
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(underscore('blue'), 'b_l_u_e')
 def test2(self):
  self.assertEqual(underscore('This is a rainy day'), 'T_h_i_s i_s a r_a_i_n_y d_a_y')
 def test3(self):
  self.assertEqual(underscore('a'), 'a')
 def test4(self):
  self.assertEqual(underscore('Sugar Plum 5!'), 'S_u_g_a_r P_l_u_m 5_!')

if __name__ == '__main__':
 unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
