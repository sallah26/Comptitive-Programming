# https://leetcode.com/problems/build-an-array-with-stack-operations/description/?envType=problem-list-v2&envId=dsa-linear-shoal-stack

target = [2,4]

n = 4

stream = list(range(n + 2))

print("Sst", stream)

stack = []

operations = []

for i in range(n):
    if(stack == target):
        # return operations
        break
    elif(stream[i + 1] in target):
        stack.append(i + 1)
        print(i + 1," in stream found")
        operations.append("Push")
        continue
    else:
        print(i + 1," in NOT stream found")
        operations.append("Push")
        operations.append("Pop")


print("stack: ", stack)

print("oops", operations)






# for i in range(n):
#     if(len(target) >= i and target[i] == i + 1):
#         operations.append("Push")
#         stack.append(i + 1)
#     else:
#         operations.append("Push")
#         # stack.append(i + 1)

#         operations.append("Pop")
#         # stack.remove(i + 1)


# print("stack: ", stack)
# # print("stack: ", )



print("oops", operations)