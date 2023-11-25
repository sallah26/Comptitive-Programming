arr = [int(i) for i in input().split(" ")[:3]]
order = input()
A = min(arr)
arr.remove(A)
C = max(arr)
arr.remove(C)
B = arr[0]
if order == "ABC":
    print(A, B, C)
elif order == "ACB":
    print(A, C, B)
elif order == "BAC":
    print(B, A, C)
elif order == "BCA":
    print(B, C, A)
elif order == "CAB":
    print(C, A, B)
elif order == "CBA":
    print(C, B, A)
else:
    print(0)