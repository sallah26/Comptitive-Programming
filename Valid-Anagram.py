# https://leetcode.com/problems/valid-anagram/

# s = "anagram"
# t = "nagaram"

s = "aacc"
t = "ccac"

if(len(s) != len(t)):
    # return false
    print("they are NOT anagram")



for i in range(len(s)):
    if(s.count(s[i]) != t.count(s[i])):
        print("they are NOT anagram")

        # counter = 
    if(s[i] not in t):
        print("they are NOT anagram")

for i in range(len(t)):
    if(t[i] not in s):
        print("they are NOT anagram")


