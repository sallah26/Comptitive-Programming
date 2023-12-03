nums = [-4,-1,0,3,10]
sort = []
for i in nums:
    # i = i * i
    sort.append(i * i)
print(sort)

for i in range(1, len(sort)):
    j = i
    while(j > 0 and sort[j] < sort[j - 1]):
        sort[j], sort[j-1] = sort[j-1], sort[j]
        j -= 1
print(sort)

