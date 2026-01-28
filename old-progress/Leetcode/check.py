# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 5 or 7:
#         return False
#     for i in range(2, int(n**2) + 1):




#     # for i in range(2, n/2):
#         if n % i == 0:
#             return False
# print(is_prime(12))

n = 11
for i in range(2, (n/2) + 1):
    if n % i == 0:
        print("The number is not prime")
    else:
        print("The number is prime")
