# ============================================
# BUT THE EASIEST WAY TO DO IS USING sorted(arr)
# ============================================

def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while(j > 0 and nums[j] < nums[j - 1]):
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums
add = [12, 43, 423, 2, 312, 42, 2423, 232, 3]
print(insertion_sort(add))

# ============================================
# BUT THE EASIEST WAY TO DO IS USING sorted(arr)
# ============================================


print(sorted(add))