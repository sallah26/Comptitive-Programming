# nums should be array
def My_Sorting_Algorithm(nums):
    sorted = []
    for i in range(len(nums)):
        sorted.append(min(nums))
        nums.remove(min(nums))
    return sorted
nums = [2,4,6,34,75,3,64,765,876]
print(My_Sorting_Algorithm(nums))