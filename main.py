class Solution(object):
    def twoNumberSum(self,array, targetSum):
        array.sort()
        left = 0
        right = len(array) - 1
        while left < right:
            currentSum = array[right] + array[left]
            if currentSum == targetSum:
                return [array[right], array[left]]
            elif currentSum > targetSum:
                right -= 1
            else:
                left += 1

        return []

test = Solution()
print(test.twoNumberSum([1,2,3,4,5],9))
