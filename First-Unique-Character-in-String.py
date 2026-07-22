# https://leetcode.com/problems/first-unique-character-in-a-string/description/

s = "lleettccoodede"

noUnique = True

for i in range(len(s)):
    current_letter = s[i]
    new_text = s.replace(current_letter, "", 1)
    if current_letter not in new_text:
        noUnique = False
        print(i)
        break

if noUnique:
    print(-1)
#     print(new_text)
    # s.replace(current_letter, "", 1)
    # print(f"new_text: {new_text}")
    # if s[i] in s:
    #     continue
    # else:
    #     print(i)
    #     break


#     if s.count(s[i]) == 1:
#         noUnique = False
#         break
#     else:
#         continue

# if noUnique:
#     print(-1)


