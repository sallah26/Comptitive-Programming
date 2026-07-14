# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=problem-list-v2&envId=array

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if(target not in nums):
            return [-1, -1]
        
        result = []
        
        starting = nums.index(target)

        ending = starting - 1

        for i in range(starting, len(nums)):
            if(nums[i] == target):
                ending = ending + 1
            else:
                break
        return [starting, ending]