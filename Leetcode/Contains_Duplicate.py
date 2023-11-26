# nums = [1,2,3,1]

# flag = bool()
# for i in nums:
#     if nums.count(i) > 1:
#         flag = True
#         break
# if flag:
#     print(True)
# else:
#     print(False)



# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

# ans = []
# for i in nums1:
#     if i in nums2:
#         ans.append(i)
# print(ans)
# for i in ans:
#     if ans.count(i) > 1:
#         ans.remove(i)
# print(ans)


# nums = [0,0]
# count = nums.count(0)
# for i in nums:
#     if i == 0:
#         nums.remove(i)
# print(count, nums)
# for i in range(count):
#     nums.append(0)
# print(nums)
# if nums.count(0) > count:
#     nums.remove(0)
#     # break

# print(nums)
# arr = [1,2,3,4,4]
# print(arr)
# arr = arr[::-1]
# print(arr)

s = "abcd"
t = "abcde"
# s = s - t
# for i in s:

# print(s)
# ms = []
# ts = []
# ans = ""
# for i in t:
#     ms.append(i)
# print(ms)
# for i in s:
#     ms.remove(i)
# print(ms)
# for i in ms:
#     ans +=i
# print(ans)


num1 = "11"
num2 = "123"

s = "selaahs dcamsd casd facledq   js,m csdcadc"

# arr = [i for i in s.split(" ")]
# print(arr)

# count = arr.count("")
# # for i in arr:
# #     if i == "":
# #         arr.remove(i)
# print(count)    
# print(len(arr) - count)
# print(arr[4])


moves = "LLU"
if moves.count("U") < moves.count("D") or moves.count("U") > moves.count("D"):
    print(False)
elif moves.count("L") < moves.count("R") or moves.count("L") > moves.count("R"):
    print(False)
else:
    print(True)