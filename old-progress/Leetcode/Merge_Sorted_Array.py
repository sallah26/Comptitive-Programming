nums1 = [1,2,3,0,0,0,]
nums2 = [2,5,6]

for i in nums1:
    if i == 0:
        nums1.remove(i)
if nums1[-1] == 0:
    nums1.remove(nums1[-1])

nums1.extend(nums2)
print(nums1)
nums1.sort()
# if 0 in nums1:
#     nums1.remove(0)
print(nums1)