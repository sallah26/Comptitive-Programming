s = "catsandog"
wordDict = ["catsan","dog","sand","and","cat"]
print(wordDict)
for i in wordDict:
    for j in wordDict:
        if i + j == s:
            print(True)