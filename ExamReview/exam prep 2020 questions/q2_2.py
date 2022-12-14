#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Flip case.
# --------------------------------------------------------------
def under(sentence):
    '''
    Assumes sentence is a string.
    Returns a string copy of string except that an underscore is added
    after each character which is not a blank and not an underscore.

    For example, 
    under('This rainy day.') returns 'T_h_i_s_ r_a_i_n_y_ d_a_y_._'  
    under('This _blue_ day.') return 'T_h_i_s_ _b_l_u_e__ d_a_y_._'  
    '''
    underSentence = ""
    for c in sentence:
      underSentence += c

      if c != '_' and c != ' ':
        underSentence += '_'
    
    return underSentence

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(under('blue'), 'b_l_u_e_')
 def test2(self):
  self.assertEqual(under('This rainy day.'), 'T_h_i_s_ r_a_i_n_y_ d_a_y_._')
 def test3(self):
  self.assertEqual(under('a'), 'a_')
 def test4(self):
  self.assertEqual(under('_red_, green, blue'), '_r_e_d__,_ g_r_e_e_n_,_ b_l_u_e_')
 def test5(self):
  self.assertEqual(under('_ _ _'), '_ _ _')
  


if __name__ == '__main__':
 unittest.main(exit=True)
