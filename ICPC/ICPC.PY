s=str(input("Enter the string ro print its suffix: "))
# s.lower()
print(s.removeprefix("sa"))
# print(s.replace("a",100))
out=""
for i in range(0,len(s)):
    if(s[i]=="a"):
        for j in range(i,len(s)):
            out+=s[j]
print(out)  
print(dir(out))
            