from random import *
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["<",">","/","?","[","]","{","}","-","@","|","$","%","&","*","(",")"]
map = [letters, numbers, symbols]
total_of_password = int(input("how many characters in your password?: "))
amount_of_numbers = int(input("how many numbers you want to have in your password?: "))
amount_of_letters = int(input("how many letters you want to have in your password?: "))
rand_of_numbers = ""
rand_of_letters = ""
rand_of_symbols = ""
password = ""
for i in range(amount_of_letters):
    rand_of_letters += choice(letters)
for i in range(amount_of_numbers):
    rand_of_numbers += choice(numbers)
for i in range((total_of_password)-(amount_of_numbers + amount_of_letters)):
    rand_of_symbols += choice(symbols)
selected = [rand_of_numbers,rand_of_letters,rand_of_symbols]
for i in range(total_of_password):
    x = randrange(len(selected))
    ranm = selected[x]
    y = randrange(len(ranm))
    password += ranm[y]
print(f"Your password is >>>>\033[96m  {password}")