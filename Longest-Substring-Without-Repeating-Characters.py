# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2074157601/

s = "c"

checker = ''
results = []
counter = 0

# if()

# for j in range(len(s)):
for i in range(len(s)):
    if(s[i] in checker):
        print(s[i], " =======")
        results.append(len(checker))
        counter = 0
        checker = s[i]
    else:
        counter = counter + 1
        checker = checker + s[i]
        print(checker)

print("results", results)
if(results):
    print(max(results))

    # return max(result)
else:
    print(0)
# print(max(results))