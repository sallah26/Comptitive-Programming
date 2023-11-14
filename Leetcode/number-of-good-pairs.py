# ----------THE PROBLEM IS HERE IN THIS LINK
# https://leetcode.com/problems/number-of-good-pairs/description/
# ---------HERE IS SOLUTION-----------#

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goods = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    goods += 1
        result = int((goods - len(nums)) / 2)
        return result

# ---------HERE IS SOLUTION LINK----------#   
# https://leetcode.com/problems/number-of-good-pairs/submissions/1098409231
# 1512. Number of Good Pairs
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0