nums = [3,2,3]
leng = int(len(nums) / 2)
for i in nums:
    countt = nums.count(i)
    if countt > leng:
        ans = i
print(ans)