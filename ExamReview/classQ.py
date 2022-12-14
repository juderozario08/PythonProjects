import unittest

# Define a class called TwoNums that has 2 attributes, “one” and “two”
    # Define an __init__method that takes 2 int parameters and stores them into "one" and "two" respectively
    # Define a method “change” that increases "one" by 1 and "two" by 2
    # Define a method “changeOne” that takes an int parameter and adds it to "one"
    # Define a method “changeTwo” that takes an int parameter and subtracts it from "two"
    # Define a method “shallowCopy” that returns a shallow copy of the method
    # Define a method “deepCopy” that returns a deep copy of the method

# --------------------------------------------------------------
# YOUR ANSWER HERE
# --------------------------------------------------------------

# --------------------------------------------------------------
# Test Cases
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(TwoNums(3,2).one, 3)
        
    def test2(self):
        self.assertEqual(TwoNums(3,2).two, 2)

    def test3(self):
        num = TwoNums(-3,-2)
        num.change()
        self.assertEqual(num.one, -2)

    def test4(self):
        num = TwoNums(-3,-2)
        num.change()
        self.assertEqual(num.two, 0)

    def test5(self):
        num = TwoNums(-23, 12)
        num.changeOne(12)
        self.assertEqual(num.one, -11)

    def test6(self):
        num = TwoNums(-23, 12)
        num.changeTwo(-32)
        self.assertEqual(num.two, 44)

    def test7(self):
        num = TwoNums(-23, 12)
        num.changeTwo(0)
        self.assertEqual(num.two, 12)

    def test8(self):
        num = TwoNums(-23, 12)
        num2 = num.shallowCopy()
        self.assertEqual(num, num2)

    def test9(self):
        num = TwoNums(-23, 12)
        num2 = num.deepCopy()
        isSame = num.one == num2.one and num.two == num2.two
        self.assertTrue(isSame)


if __name__ == '__main__':
    unittest.main(exit=True)