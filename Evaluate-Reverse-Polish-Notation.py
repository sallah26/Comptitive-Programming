# https://leetcode.com/problems/evaluate-reverse-polish-notation/?envType=problem-list-v2&envId=dsa-linear-shoal-stack

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

stack = []
operators = {"+", "-", "*", "/"}

for token in tokens:
    if token not in operators:
        stack.append(int(token))
    else:
        right = stack.pop()
        left = stack.pop()

        if token == "+":
            result = left + right
        elif token == "-":
            result = left - right
        elif token == "*":
            result = left * right
        else:
            result = int(float(left) / right)
        stack.append(result)

result = stack[0]

print(result)