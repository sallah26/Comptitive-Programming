l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

reversed_l1 = l1[::-1]
reversed_l2 = l2[::-1]

string_rev_l1 = ""
string_rev_l2 = ""

for i in reversed_l1:
    string_rev_l1 += str(i)

for j in reversed_l2:
    string_rev_l2 += str(j)
num_rev_l1 = int(string_rev_l1)
num_rev_l2 = int(string_rev_l2)

thir_sum = num_rev_l1 + num_rev_l2

thir_sum_arr = []
thir_sum = str(thir_sum)
for y in thir_sum:
    thir_sum_arr.append(int(y))

thir_sum_rev = thir_sum_arr[::-1]
print(thir_sum_rev)
# print(type(thir_sum))