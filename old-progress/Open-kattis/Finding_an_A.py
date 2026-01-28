inp = input()
arr = []
for i in inp:
    arr.append(i)
print(arr)

for j in arr:
    if j == "a":
        print(arr)
        print("Yesss")
        break
    else:
        arr.remove(j)
print(arr)
