p = [1,2,3,4]
q = [12,21,2,4]
if len(p) != len(q):
    print(False)
elif len(p) == len(q):
    for i in len(p):
        if p[i] != q[i]:
            print(False)
else:
    print(True)
        # for j in q:
