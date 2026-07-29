x = 10

def IsPalendrom(x):
    # This solution is after i learn about two pointers and look how easy it is 
    strX = str(x)
    left = 0
    right = len(strX) - 1

    for i in range(len(strX)):
        # print(strX[i])
        if(strX[left] == strX[right]):
            left += 1
            right -= 1
        else:
            return False
            break
    return True

    # middle = len(title) // 2

    # # print(middle)
    # if(len(title) % 2 == 1):
    #     first_half = title[0:middle + 1]
    # else:
    #     first_half = title[0:middle]

    #     # middle =+ 1


    # # first_half = title[0:middle]
    # second_half = title[middle:]
    # second_half = second_half[::-1]

    # # print("first half: ", first_half)
    # # print("second half: ", second_half)

    # if(first_half == second_half):
    #     # print("Yup palindrom!")
    #     return True
    # else:
    #     return False
   

print(IsPalendrom(x))