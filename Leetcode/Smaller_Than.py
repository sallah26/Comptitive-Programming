nums = [8,1,2,2,3]
# for i in nums:
arr = []
for i in range(len(nums)):
    print(nums[i])
    count = 0
    for j in range(len(nums)):
        if nums[j] < nums[i]:
            count += 1
    arr.append(count)
print(nums)
print(arr)
