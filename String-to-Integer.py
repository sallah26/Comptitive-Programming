# https://leetcode.com/problems/string-to-integer-atoi/description/
# Pseudocode

# 1, Trime any whitespaces will use // lstripe
# 2, determine the posativity of the number by checking if -  is there in the leading, 
# 3, Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# 4, round the integer to be between the range of [-231, 231 - 1]
# 5, Return plain integer

s = s.lstrip()
if not s:
    return 0

isNegative = False

# 1. Handle signs safely
if s[0] == "-":
    isNegative = True
    s = s[1:]
elif s[0] == "+":
    s = s[1:]

# 2. Build the number mathematically inside the loop
result = 0
for char in s:
    if not char.isdigit():
        break
    else:
        # Convert the single character to its number and add it to the total
        digit_value = ord(char) - ord('0')
        result = (result * 10) + digit_value

# 3. Apply the sign
if isNegative:
    result = -result

# 4. Handle LeetCode's strict 32-bit integer limits
INT_MIN = -2147483648
INT_MAX = 2147483647

if result < INT_MIN:
    return INT_MIN
if result > INT_MAX:
    return INT_MAX

return result