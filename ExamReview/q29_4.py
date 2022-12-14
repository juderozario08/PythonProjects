#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
class HungryHippo:
    '''
    Implement the __init__ function for a HungryHippo class, where
    each HungryHippo has a string "colour" that is an argument
    to its __init__ function. Additionally, each HungryHippo should have
    an int "grass_eaten" that starts at 0.

    Then create an instance method eat_grass(g) which adds an integer g 
    to the HungryHippo's grass_eaten.

    Then, implement the method below.
    '''
    def __init__(self, colour) :
        # GIVEN CODE
        self.colour = colour
        self.grass_eaten = 0
        pass
    def eat_grass(self, g) :
        # YOUR CODE GOES HERE
        self.grass_eaten += g
    pass
def hungriest_hippo(list_of_hippos):
    '''
    Assumes list_of_hippos is a nonempty list of Hungry_Hippo objects.
    Changes the colour of the HungryHippo who has eaten the most grass
    to the string "green", and returns the HungryHippo who
    has eaten the least grass.

    For example, imagine you create a HungryHippo h1 with colour "blue"
    (via the syntax: h1 = HungryHippo("blue"), a HungryHippo h2 with 
    colour "purple", and a HungryHippo h3 with colour "turquoise". Then you 
    call h1.eat_grass(2), and h2.eat_grass(3). When you call the method 
    hungriest_hippo([h1, h2, h3]), it should change h2's colour 
    to "green", and return h3.
    '''
    # YOUR CODE GOES HERE
    least = None
    most = None
    for i in list_of_hippos:
        if most == None or i.grass_eaten > most:
            most = i.grass_eaten
            fatHippo = i
        if least == None or i.grass_eaten <least:
            least = i.grass_eaten
            skinnyHippo = i
    fatHippo.colour = "green"
    return skinnyHippo

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        h1 = HungryHippo("blue")
        self.assertEqual(h1.colour, "blue")
        self.assertEqual(h1.grass_eaten, 0)
    def test2(self):
        h1 = HungryHippo("blue")
        h1.eat_grass(3)
        self.assertEqual(h1.grass_eaten, 3)
    def test3(self):
        h1 = HungryHippo("blue")
        h1.eat_grass(3)
        h1.eat_grass(2)
        self.assertEqual(h1.grass_eaten, 5)
    def test4(self):
        h1 = HungryHippo("blue")
        h2 = HungryHippo("purple")
        h3 = HungryHippo("turquoise")
        h1.eat_grass(4)
        h2.eat_grass(5)
        self.assertEqual(hungriest_hippo([h1, h2]), h1)
    def test5(self):
        h1 = HungryHippo("blue")
        h2 = HungryHippo("purple")
        h3 = HungryHippo("turquoise")
        h1.eat_grass(4)
        h2.eat_grass(5)
        ans = hungriest_hippo([h1, h2, h3])
        self.assertEqual(h2.colour, "green")
    def test6(self):
        h1 = HungryHippo("blue")
        h2 = HungryHippo("purple")
        h3 = HungryHippo("turquoise")
        h1.eat_grass(6)
        h2.eat_grass(5)
        ans = hungriest_hippo([h1, h2, h3])
        self.assertEqual(h1.colour, "green")
        self.assertEqual(ans, h3)
if __name__ == '__main__':
 unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
