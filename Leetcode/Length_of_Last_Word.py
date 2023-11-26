s = "   fly me   to   the moon  "
arr = [i for i in s.split(" ")]
arr2 = []
for i in arr:
    if len(i) > 0:
        arr2.append(i)
print(len(arr2[-1]))