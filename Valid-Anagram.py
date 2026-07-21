# https://leetcode.com/problems/valid-anagram/

s = "anagram"
t = "nagaram"

# s = "aacc"
# t = "ccaa"

# if(len(s) != len(t)):
#     # return false
#     print("they are NOT anagram")

# for i in range(len(s)):
#     if(s.count(s[i]) != t.count(s[i])):
#         print("they are NOT anagram")

#         # counter = 
#     if(s[i] not in t):
#         print("they are NOT anagram")

# for i in range(len(t)):
#     if(t[i] not in s):
#         print("they are NOT anagram")


# boom this lets me to change my mind, found it with one of the LLMs, actually it shows the power of dictionaries, then i like that huh, learnt how it works and loved it 
def isAnagram(s: str, t: str) -> bool:
    # 1. Quick length check (Your excellent first rule!)
    if len(s) != len(t):
        return False

    # 2. Build frequency counters using dictionaries
    countS = {}
    countT = {}

    for i in range(len(s)):
        # If the letter isn't in the dict yet, start at 0, then add 1
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1

    # 3. Simply compare the two dictionaries
    # Python automatically checks if they have the exact same keys and values!
    print("yes sir")
    print("countS: ", countS)
    print("countT: ", countT)
    return countS == countT

isAnagram(t, s)