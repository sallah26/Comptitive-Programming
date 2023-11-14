import random
str=["ethiopia","africa","asia","worabe","dubai"]
ranstr=random.choice(str)
y=len(ranstr)-1
underscor1=[" _ "]
for i in range(y):
    underscor1.append(" _ ")
inp=input("enter the letter to check wearher it is ther in the given word: ")
for i in range(y+1):
    if(ranstr[i]==inp):
        underscor1[i]=ranstr[i]
        print("You win! correctly gussed")
print(underscor1)    
