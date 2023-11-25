my_dict = {
"a":"@",
"b":"8",
"c":"(",
"d":"|)",
"e":"3",
"f":"#",
"g":"6",
"h":"[-]",
"i":"|",
"j":"_|",
"k":"|<",
"l":"1",
"m":"[]\/[]",
"n":"[]\[]",
"o":"0",
"p":"|D",
"q":"(,)",
"r":"|Z",
"s":"$",
"t":"']['",
"u":"|_|",
"v":"\/",
"w":"\/\/",
"x":"}{",
"y":"`/",
"z":"2"
}
num = input()
num = num.lower()
ans = ""
for i in num:
    if i in my_dict:
        ans += my_dict[i]
    else:
        ans += i
if ans[-1] != "!":
    ans += "!"
print(ans)
