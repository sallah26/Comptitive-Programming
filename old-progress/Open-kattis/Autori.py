name = input()
name_arr = name.split("-")
ans = ""
for i in name_arr:
    ans += i[0]
print(ans)