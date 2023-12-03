# # class Node:
# # 	def __init__(self, data):
# # 		self.data = data
# # 		self.next = None
# #         def insertAtBegin(self, data):
# #             new_node = Node(data)
# #             if self.head is None:
# #                 self.head = new_node
# #                 return
# #             else:
# #                 new_node.next = self.head
# #                 self.head = new_node
# print("Hello world")


# # print(arr[2::2])
# # print(arr[2::6])

# arr = []
# nums = [-1,0,1,2,-1,-4]
# for i in nums:
#     for j in nums:
#         for k in nums:
#             if i + j + k == 0:
#                 arr.append([i,j,k])
# # print(arr)
# # for i in range(len(arr)-2):
# #     if arr[i] == arr[i + 1]:
# #         arr.remove(arr[i] + 1)
# # print(arr)

# for i in arr:
#     if arr.count(i) > 1:
#         arr.remove(i)
# # print(arr)
# length = len(arr) - 1
# # print(arr[0][0])
# sol = []
# print(arr[length])
# for i in range(length):
#     for j in range(1, length):
#         # for k in range(0, 2):
#         if i != j:
#             print(i,j)
#             if arr[i][0] in arr[j] and arr[i][1] in arr[j] and arr[i][2] in arr[j]:
#                 print(i,j)
#                 # arr.remove(arr[j])
#                 sol.append(arr[j])
#                 print("Exists in another!")
# print(sol)
# for i in sol:            
#     for j in sol:
#         if sol.count(i) > 1 and i == j:
#             sol.remove(i)

# print(sol)
#         # print(i,j)
#         # if arr[i][0] in arr[j] and arr[i][1] in arr[j] and arr[i][2] in arr[j]:
#         #     arr.remove(arr[j])



# nums = [1,1,1,1]

# for i in nums:
#     if nums.count(i) > 1:
#         nums.remove(i)

# for i in nums:
#     if nums.count(i) > 1:
#         nums.remove(i)
# print(len(nums))
# print(nums)



nums = [53,71,7,82,0, 23343, 8,10]
# target = 8
# if nums == [0]:
#     return [0, 0]
# elif target in nums:
#     bzat = nums.count(target)
#     indx = nums.index(target)
#     arr = []
#     for i in range(bzat):
#         arr.append(indx)
#         indx +=1
#     print(arr)
# else:
#     print([-1,1])
# print(sorted(nums))

# ==================IT IS WORKING===================
# name = "selahadi"
# subs = []
# max = 0
# maxs = []
# arr = [1, 3, 5, 8, 1, 23, 65, 897]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i != j:
#             subs.append([arr[i], arr[j]])
# for k in subs:
#     maxs.append(k[0] + k[1])
# print(maxs)
# maxs = sorted(maxs)
# print("The maximium : = ",maxs[-1])

# ==================IT IS WORKING===================


# arr = [1, 3, 5, 8, 1, 7, 21, 2]
# should = 16

# for i in range

nums = [0,1,0,3,12]
nums2 = []

for i in range(len(nums) - 1, -1, -1):
    if nums[i] == 0:
        nums2.append(0)
        nums.remove(nums[i])

print(nums + nums2)