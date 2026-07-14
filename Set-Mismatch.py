# nums = [1,1]
# https://leetcode.com/problems/set-mismatch/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii



# nums = [1,2,3,3]
# nums = [1,2,3,4,5,6,7,8,8,10]


# nums = [2,3,2]
nums = [1,3,3,4]

result = []

nums.sort()

# for i in range(len(nums) - 1):
#     if(nums[i] == nums[i+1]):
#         result.insert(0, nums[i])
#         result.insert(1, nums[i + 1])
#         print("inserting one", result)
#         if(nums.count(1) == 0):
#             result = [2,1]
# print("final result", result)


for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        duplicate = nums[i]
        break

for i in range(1, len(nums) + 1):
    if i not in nums:
        missing = i
        break

print("final answer",[duplicate, missing])