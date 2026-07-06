# problem url: https://leetcode.com/problems/concatenation-of-array/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

class Solution(object):
    def getConcatenation(self, nums):
       
        ans = []

        for i in range(2):
            for j in range(len(nums)):
                ans.append(nums[j])
        return ans

print("new ans", Solution().getConcatenation(nums = [1,2,3,4,5,6,7]))

