nums = [-4, -1, 0, 3, 10]

for i in range(len(nums)):
    nums[i] = nums[i] * nums[i]

nums = nums.sort()
print("nums: ", nums)
