nums = [2,5,1,3,4,7]
n = 3

nums_front = nums[0:n]
nums_back = nums[n:]

result = []

for i in range(len(nums_front)):
    result.append(nums_front[i])  
    result.append(nums_back[i])  

print("result: ", result)
