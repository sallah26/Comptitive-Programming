data = "\/\/in_US$100000_in_our_Ca$h_Lo||ery!!!"
upper = 0
lower = 0
symbol = 0
space = 0
for i in data:
    if i.isupper():
        upper +=1
    elif i.islower():
        lower +=1
    elif i == ("_"):
        space +=1
    else:
        symbol +=1
        # print()
# print("upper: ", upper, "lower: ", lower, " symbols: ",  symbol, "spaces: ", space)
print(space/len(data))
print(lower/len(data))
print(upper/len(data))
print(symbol/len(data))
# print()