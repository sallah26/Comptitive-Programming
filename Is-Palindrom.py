name = "aba"

def IsPalendrom(title):
    middle = len(title) // 2

    # print(middle)
    if(len(title) % 2 == 1):
        first_half = title[0:middle + 1]
    else:
        first_half = title[0:middle]

        # middle =+ 1


    # first_half = title[0:middle]
    second_half = title[middle:]
    second_half = second_half[::-1]

    # print("first half: ", first_half)
    # print("second half: ", second_half)

    if(first_half == second_half):
        # print("Yup palindrom!")
        return True
    else:
        return False
   

print(IsPalendrom(name))