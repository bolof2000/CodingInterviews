from collections import defaultdict
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

    def randomNote(self,magazine,word):
      dic = defaultdict(int)
      for char in magazine:
        dic[char] +=1
      
      for c in word:
        if dic[c] <=0:
          return False
        dic[c] -=1
      return True


    def randomNote2(self,magazine,word):
      check = all(item in word for item in magazine)

      return check


    def duplicateNumber(self,nums):

      occurrence = {}
      for num in nums:
        occurrence[num] = occurrence.get(num,0)+1
        for key,value in occurrence.items():
          if value ==1:
            return key   

    def duplicateNumber2(self,nums):
      unique =0
      for num in nums:
        unique ^=num 

      return unique

         



test = Solution()
magazing = ['A','B','C','D','E','F','D','F']
#dic = {A:1,B:1,C:1,D:2,F:2}
word = "DFDDF"
#print(sorted(list(word)))
#print(sorted(magazing))
print(test.randomNote(magazing,word))
print(test.randomNote2(magazing,word))
#print(test.twoNumberSum([1,2,3,4,5],9))
print(test.duplicateNumber2([1,2,3,4,5,1,2,3,4]))
