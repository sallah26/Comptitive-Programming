# https://leetcode.com/problems/longest-common-prefix/?envType=problem-list-v2&envId=array

strs = ["flower","flow","flight"]

prefix = ""

for i in range(len(strs[0])):

    for word in strs[1:]:

        if i >= len(word) or word[i] != strs[0][i]:
            return prefix
            print([prefix])

    prefix += strs[0][i]

print(prefix)


# # commonPrefix = ''
# commonPrefix = strs[0][0]

# minStrLength = 200
# for str in strs:
#     if len(str) < minStrLength:
#         minStrLength = len(str)

# # print(minStrLength)

# # print("common: ", commonPrefix)

# # for str in strs:
# for i in range(len(strs)):
#     print("cmm", commonPrefix)
#     for str in strs:
#         if(commonPrefix == ''):
#             break
#         elif(commonPrefix == i):
#             print(str[i])
#         else:
#             commonPrefix == ''

# print("common prefix : ", commonPrefix)
# # for str in strs:
# #     for i in range(len(strs)):
# #         print("dd")
#         # if(str[0])


# strs = ["flower","flow","flight"]

# common = strs[0][0]

# minStrLength = 200
# for str in strs:
#     if len(str) < minStrLength:
#         minStrLength = len(str)


# for i in range(minStrLength):
#     for str in strs:
#         print("checking .. ", str)
#         if(str[i] == common[-1]):
#             print("checking inside", common[-1])
#             if(common[-1] != str[i]):
#                 common = "{common}{str[i]}"

# print("comm : ", common)