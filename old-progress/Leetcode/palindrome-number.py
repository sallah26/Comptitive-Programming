# ----------THE PROBLEM IS HERE IN THIS LINK
# https://leetcode.com/problems/palindrome-number/description/
# ---------HERE IS SOLUTION-----------#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        reversed = strx[::-1]
        if (reversed == str(x)):
            return True
        else:
            return False

# ---------HERE IS SOLUTION LINK----------#
# https://leetcode.com/problems/palindrome-number/submissions/1098471924

# 9. Palindrome Number
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

#  Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

