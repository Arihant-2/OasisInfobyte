import string
import random

# Getting password length
P_len = int(input("Enter the password length of your choice: "))

print('''Select character set for your random password from these keys: 
        1. Add letters in the random password
        2. Add digits in the random password
        3. Add special characters in the random password
        4. Exit''')

elements = ""

# Getting character set for password
while True:
    Key = int(input("Enter a number among 1, 2, 3, or 4 as key to change password: "))
    if Key == 1:
        # Adding letters to the password randomly 
        elements += string.ascii_letters
    elif Key == 2:
        # Adding digits to the password randomly
        elements += string.digits
    elif Key == 3:
        # Adding special characters to the password
        elements += string.punctuation
    elif Key == 4:
        break
    else:
        print("Please type a valid Key ... !")

# Generating password
passwd = []

for j in range(P_len):
    randomchar = random.choice(elements)
    # Appending a random character to password
    passwd.append(randomchar)

# Result
print("Your random password is: " + "".join(passwd))

