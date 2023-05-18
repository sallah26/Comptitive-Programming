user_need=input("What would you like? (espresso/latte/cappuccino): ")
if user_need == "espresso" or "latte" or "cappuccino":
    y=5
elif user_need == "off":
    exit()
else:
    print("Invalid input!")
    exit()
report = {
   "Water": 100,
    "Milk": 50,
    "Coffee": 76,
    "Money $": 0 
}

resource = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100
}
if user_need == "espresso":
    if resource["Water"] < 50 or resource["Coffee"] < 18:
        print("There is not enough resource in the machin!")
        exit()
    else:
        resource["Water"]-=50
        resource["Coffee"]-=18 

print(resource)
