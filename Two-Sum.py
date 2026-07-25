# # nums = [3,3]
# nums = [2,7,11,15]
# target = 9

# seen_numbers = {}


# for i in range(len(nums)):
#     complement = target - nums[i] 
#     if(complement in seen_numbers):
    
#         # Loop to find the key
#         found_key = None
#         for key, value in seen_numbers.items():
#             if key == complement:
#                 found_key = key
#                 print(found_key)
#                 break
#         print([i, found_key])
#     else:
#         seen_numbers.update({nums[i] : i})




# # this was old try but confused what it's issue was
# # for i in range(len(nums)):
# #     complement = target - nums[i] 
# #     if(complement in seen_numbers):
# #         print("yes it is there : ",complement," and ", nums[i])
# #         print([complement,  i])
# #     else:
# #         seen_numbers.update({nums[i] : i})

# # print(seen_numbers)


# nums = [3,3]
nums = [5, 12, 2, 7, 11, 15]
target = 9








# seen_numbers = {}

# for i in range(len(nums)):
#     complement = target - nums[i]
    
#     if complement in seen_numbers:
#         complement_index = seen_numbers[complement]
        
#         print([complement_index, i]) 
#         break  
#     else:
#         seen_numbers[nums[i]] = i

# print(seen_numbers)

