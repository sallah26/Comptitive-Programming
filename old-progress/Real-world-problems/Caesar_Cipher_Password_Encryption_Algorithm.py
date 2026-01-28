# The decoration part just for decoration only :)
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("|===========================================================================================================|")
print("|===========================================================================================================|")
print("|======---------=======|-----------------------------------------------------------|=========---------======|")
print("|======|       |=====   (: WELL COME TO PASSWORD ENCRYPTION AND DECRYPTION PROGRAM :)  ======|        |=====|")
print("|======---------=======|-----------------------------------------------------------|==========---------=====|")
print("|===========================================================================================================|")
print("|===========================================================================================================|")
print(" ")
print(" ")




# Here the logic will go
Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
task = int(input("Enter 1 for Password ENCRYPTION or 2 Password for DECRYPTION: "))

if task == 1:
    plain_text = input("Greate!, Please Enter Your Text To Encrypt: ").lower()
    cipher_text = ""
    for i in plain_text:
        if i != " ":
            index = Letters.index(i)
            if index == 23:
                cipher_text += "a"
            elif index == 24:
                cipher_text += "b"
            elif index == 25:
                cipher_text += "c"
            else:
                cipher_text += Letters[index + 3]
        else:
            cipher_text += " "
    print(" ")
    print(f"Your Encrypted Password is Here Between The Two Brackets [{cipher_text}]")
    print("                                                        ----------------")
    print("Thanks For Working With Us!")
    print(" ")
    print(" ")
elif task == 2:
    cipher_text = input("Please Enter Your Text To Decrypt: ").lower()
    plain_text = ""
    for i in cipher_text:
        if i != " ":
            index = Letters.index(i)
            if index == 2:
                plain_text += "z"
            elif index == 1:
                plain_text += "y"
            elif index == 0:
                plain_text += "x"
            else:
                plain_text += Letters[index - 3]
        else:
            plain_text += " "
    print(" ")
    print(f"Your Decrypted Password is Here Between The Two Brackets [{plain_text}]")
    print("                                                        ----------------")
    print("Thanks For Working With Us!")
    print(" ")
    print(" ")
else:
    print("Please Enter only number 1 or 2!")