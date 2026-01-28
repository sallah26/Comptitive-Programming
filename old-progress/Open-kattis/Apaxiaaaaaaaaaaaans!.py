string = input()

result = ""
previous_char = None
for char in string:
    if char != previous_char or len(result) == 0 or result[-1] != char:
        result += char
    previous_char = char

print(result)
