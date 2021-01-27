import unittest
from main import Solution
class TestSolutions(unittest.TestCase):

  def testProductSum(self):

    test = Solution()
    nums = [1,2,3,4,5]
    actual = [120,60,40,30,1]

    expected = test.productArrayExceptItself(nums)
    self.assertEqual(expected,actual)

if __name__ == '__main__':
  unittest.main()



