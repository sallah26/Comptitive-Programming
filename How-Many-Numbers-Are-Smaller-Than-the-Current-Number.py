# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

nums = [8,1,2,2,3]

result = []
for j in nums:
    counter = 0
    for i in range(len(nums)):
        if(nums[i] < j):
            counter = counter + 1
    result.append(counter)

print("result = ", result)

