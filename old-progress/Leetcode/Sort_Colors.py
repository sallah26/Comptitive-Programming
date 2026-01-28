nums = [2,0,1]

for i in range(1, len(nums)):
    j = i
    while (j > 0 and nums[j] < nums[j - 1]):
        nums[j], nums[j - 1] = nums[j - 1],nums[j]
        j -= 1
print(nums)