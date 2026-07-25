from enum import unique
s = ")()())"

def longestValidParentheses(s: str) -> int:

    s = s + " "
    for i in range(len(s)):
        if(s[i] == " "):
            break
        elif((s[i] == "(") and (s[i + 1] == ")")):
            s.replace("()","")


            

    # openBrackets = s.count("(")
    # closeBrackets = s.count(")")
    # print("openBrackets: ", openBrackets)
    # print("closeBrackets: ", closeBrackets)
    
    
print(longestValidParentheses(s))




# 1, Payment phase update eyesera adelem
# 2, Phone number must be prrovided in the time of client case creation
# # 3, name of the user must also become unique
# 4, 
