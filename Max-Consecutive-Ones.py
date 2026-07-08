# https://leetcode.com/problems/max-consecutive-ones/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

nums = [1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,0]

max_consecutive = 0
current_count = 0

for i in nums:
    if i == 1:
        current_count += 1
        if current_count > max_consecutive:
            max_consecutive = current_count
    else:
        current_count = 0

print("so max is", max_consecutive)