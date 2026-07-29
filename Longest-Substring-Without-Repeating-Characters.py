# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2074157601/

# s = "c"

# checker = ''
# results = []
# counter = 0

# # if()

# # for j in range(len(s)):
# for i in range(len(s)):
#     if(s[i] in checker):
#         print(s[i], " =======")
#         results.append(len(checker))
#         counter = 0
#         checker = s[i]
#     else:
#         counter = counter + 1
#         checker = checker + s[i]
#         print(checker)

# print("results", results)
# if(results):
#     print(max(results))

#     # return max(result)
# else:
#     print(0)
# # print(max(results))


# AFTER WE LEARN TWO POINTERS


s = "pwxwkew"

seen = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])
    max_len = max(max_len, right - left + 1)

print(max_len)