import unittest
# Create a function "sortNums" that given a list of integers, returns a dictionary where the key is the ten's column, and the value is a list of the one's column.
    # ex input: [13, 15, 78, 44, 21, 97, 4, 13, 78]
    # ex output:  {1: [3, 5, 3], 7: [8, 8], 4: [4], 2: [1], 9: [7], 0: [4]}

# --------------------------------------------------------------
# YOUR ANSWER HERE
# --------------------------------------------------------------

def sortNums(nums):
    sorted = {}
    for num in nums:
        key = num // 10
        value = num % 10
        if (key in dict.keys(sorted)):
            sorted[key].append(value)
        else:
            sorted[key] = [value]
    
    return sorted


# --------------------------------------------------------------
# Test Cases
# --------------------------------------------------------------

class myTests(unittest.TestCase):
    def sameAnswer(self, numDict, numDict2):
        if (len(dict.keys(numDict)) != len(dict.keys(numDict2))):
            return False
        
        for key in dict.keys(numDict):
            if (len(numDict[key]) != len(numDict2[key])):
                return False
            for i in range(len(numDict[key])):
                if (numDict[key][i] != numDict2[key][i]):
                    return False
        
        return True

    def test1(self):
        sorted = sortNums([13, 15, 78, 44, 21, 97, 4, 13, 78])
        self.assertTrue(self.sameAnswer(sorted, {1: [3, 5, 3], 7: [8, 8], 4: [4], 2: [1], 9: [7], 0: [4]}))
        
    def test2(self):
        self.assertEqual(sortNums([]), {})
    
    def test3(self):
        self.assertEqual(sortNums([1]), {0: [1]})

    def test4(self):
        self.assertEqual(sortNums([1,1,1,1]), {0: [1, 1, 1, 1]})

if __name__ == '__main__':
    unittest.main(exit=True)
