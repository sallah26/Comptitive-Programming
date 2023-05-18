# #PARITY SORT
# x = int(input())
# odd = []
# even = []
# bothh = []
# list1 = [int(val) for val in input().split()[:x]]
# for i in list1:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# even.sort()
# bothh.extend(even)
# odd.sort()
# bothh.extend(odd)
# for i in bothh:
#     print(i,end=" ")


##BACK TO BASICS
# x = input()
# mul = 1
# bothh = []
# sum = 0
# for i in x:
#     bothh.append(int(i))
# for j in bothh:
#     mul*=j
#     sum+=j
# print(mul-sum)


# ##PAIR PRODUCTS
# x = int(input())
# vals = []
# list1 = [int(val) for val in input().split()[:x]]
# for i in range(x-1):
#     y = 1
#     x = list1[i]
#     j = list1[i+1]
#     y = x*j
#     vals.append(y)
# print(max(vals))


x = int(input())
list1 = []
list2 = []
for i in range(x):
    list1.append(input())
for j in list1:
    for k in j:
        while k =="O":
            i = 0
            i+=1
        list2.append(i)
print(list1)
print(list2)