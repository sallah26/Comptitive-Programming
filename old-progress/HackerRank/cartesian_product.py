A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
# B = [3, 4]

ans = []
for i in A:
    for j in B:
        print((i , j), end=" ")
# for i in range(len(A)):
#     for j in range(len(B)):
#         ans.append(())
print(ans)