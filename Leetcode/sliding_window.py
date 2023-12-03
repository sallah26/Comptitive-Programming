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

def slide(str, indx):
    ans = []
    if len(str) <= 2:
        return str
    for i in range(len(str) - (indx + 1)):
        ans.append(str[i:i+indx])
    return ans
print(slide(stri, 5))

# stri = [1, 2, 3, 4, 5, 6, 7, 7, 7, 45, 54, 34, 4]
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









