s = "Helloworld"

stri = [1, 2, 3, 4, 5, 6, 7, 7, 7, 45, 54, 34, 4]
# def slide(s, indx):
#     ans = []
#     if len(s) <= 2:
#         return s
#     for i in range(len(s) - (indx + 1)):
#         ans.append(s[i:i + indx])
#     return ans
# print(slide(s, 3))

# def slide(str, indx):
#     ans = []
#     if len(str) <= 2:
#         return str
#     for i in range(len(str) - (indx + 1)):
#         maxx = sum(str[i:i+indx])
#         print(maxx)
#         ans.append(maxx)

#     return ans
# print(slide(stri, 5))

k = 3
current_max = 0
stri = [1, 2, 3, 4, 5, 6, 777, 7, 7, 45, 54, 34, 4]
for i in range(len(stri)):
    print(stri[i:k + i])
    current_max = max(sum((stri[i:k + i])), current_max)
    print(current_max)

# print(min(stri))
# def slide(string, k):
#     if len(string) < k:
#         return string
#     max = 0
#     submax = sum(string[:k])
#     for i in range(len(string) - k):
#         print(sum(string[i:i + k]))
#         print(max(string[i:i + k]))
#         # submax = max(sum(string[i:i + k]), submax)
#     return submax

# print(slide(stri, 4))
# my_dict = {
#     "id":1,
#     "name":"selahadin",
#     "school":"ASTU",
#     "colleg":"04"
# }


# print(my_dict)
# print(my_dict.keys())
# # print(arr)
# my_dict["id"] = 3
# print(my_dict)

# def longest_increasing_subarray(nums):
#     start = 0
#     end = 0
#     longest_subarray = []

#     while end < len(nums):
#         if end > 0 and nums[end] <= nums[end - 1]:
#             # Reset the start pointer and update the longest subarray if a decreasing element is found
#             start = end

#         current_subarray = nums[start:end + 1]

#         if len(current_subarray) > len(longest_subarray):
#             # Update the longest subarray if the current subarray is longer
#             longest_subarray = current_subarray

#         end += 1

#     return longest_subarray