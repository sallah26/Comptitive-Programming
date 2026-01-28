# x = int(input("enter: "))
# list1 = [3]
# bol = True
# for k in range(5,x,1):
#     print("k = ",k)
#     for i in range(2,int(k/2),1):
#         print("k = ",k)
#         print("i = ",i)
#         if k%i == 0:
#             bol = False
#         else:
#             list1.append(k)
# print(list1)


# x = int(input("enter: "))
# if bol:
#     print("The number is prime")
# else:
#     print("The number is not prime")

# my_list = [1,2]
# x = int(input())
# for i in range(x):
#     my_list.append(my_list[i]+my_list[i+1])
# print(my_list)

# def fub(my_list):
#     return my_list[-1]+my_list[-2]

# def add(x,y):
#     print(x+y)

# print(lambda x,y :x+y)


# def filt(x):
#     return x>50
# my_list = [1,2,4,5,78,345,34]
# filtered_list = filter(filt, my_list)
# print(list(filtered_list))


# my_list = [1,2,4,5,78,345,34]
# filtered_list = list(filter(lambda x:x>50, my_list))

# print(filtered_list)



# my_list = [
#     {"name":"harun1", "age":30},
#     {"name":"harun2", "age":23},
#     {"name":"harun3", "age":45},
#     {"name":"harun4", "age":23},
#     {"name":"harun5", "age":20},
#     {"name":"harun6", "age":23},
#     {"name":"harun7", "age":30},
#     {"name":"harun8", "age":20},
# ]

# filtered_list = list(filter(lambda user: user["age"] > 20 and user["age"] < 30, my_list))
# print(filtered_list)

# user = {
#     "fname":"juck",
#     "lname":"jon",
#     "age":56,
#     "address":{
#         "country":"ethiopia",
#         "state":"oeoe",
#         "city":"adama",
#     },
#     "is_active":False
# }

# print(user)
# user = {**user, "is_active":True}
# print(user)

# filtered_list = []
# for user in my_list:
#     if  user["age"] > 20 and user["age"] < 30:
#         filtered_list.append(user)
# print(filtered_list)

# updated_list = list(map(lambda user: {**user, "age": 20} , my_list))
# print(updated_list)


# def add(x=0,y=10):
#     return x+y
# key = "x"
# value = 23

# par = {key:value}


# print(add(**par))


# from functools import reduce


# my_list = [1,2,4,5]
# reduced_val = reduce(lambda pev, x: pev * x, my_list)
# print(reduced_val)


# from itertools import groupby

# groupbyed = groupby(my_list, lambda user: user["age"])
# for age,user in groupbyed:
#     print(age,user)
# def deepsearch(array, value):
#     ind = []
#     i = 0
#     for val in array:
#         if type(val) == list:
#             index = deepsearch(val, value)
#             if len(index):
#                 ind.append([i,*index])
#         elif val == value:
#             ind.append(i)
#         i+=1
#     return ind

# my_list = [[23,34,56, [54,6,8],[5,4,6]],[54,76], 35]

# print(deepsearch(my_list, 6))
list = []
bol = False
x = int(input())
for i in range(3,x):
    for j in range(2,i//2):
        print("i1 and j1: ", i , j)
        if i%j==0:
            bol = True
            print("i and j: ", i , j)
    if bol:
        list.append(i)
print(list)


