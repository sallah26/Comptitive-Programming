# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix)
# [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
# ans = []

# matrix = matrix[::-1]
# # for i in matrix:
#     # ans.append([i[-1],i[-2],i[-3]])
# for j in matrix:
#     for i in range(len(matrix)):
#         ans.append(j[i])
# print(ans)

# print(matrix[0][2])
# print(len(matrix))
# ans = []
# for i in range(len(matrix) -1):
#     for j in range(len(matrix) -1):
        
nums = [1]
for i in nums:
    if nums.count(i) < 2:
        print(i)