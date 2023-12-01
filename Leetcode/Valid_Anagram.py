s = "a"
t = "ab"

flag = True
for i in s:
    if (i in t) and (s.count(i) == t.count(i)) and (len(s) == len(t)): 
        pass
    else:
        flag = False
        break

if flag == True:
    print(True)
else:
    print(False)
    # else:
    #     print(False)