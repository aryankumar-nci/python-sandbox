import random

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
           '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '<',
           '.', '>', '/', '?', '|', '`', '~']

letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the PyPassword Generator:\n")

# Get user inputs
num_letters = int(input("How many letters do you want in your password?\n"))
num_symbols = int(input("How many symbols do you want in your password?\n"))
num_numbers = int(input("How many numbers do you want in your password?\n"))

# # Easy level
# password = ""
#
# for char in range(num_letters):
#     password += random.choice(letters)
#
# for char in range(num_symbols):
#     password += random.choice(symbols)
#
# for char in range(num_numbers):
#     password += random.choice(numbers)
#
# print("Your generated password is:", password)
#

#Hard level

password_list    = []

for char in range(num_letters):
    password_list.append(random.choice(letters))

for char in range(num_symbols):
    password_list.append(random.choice(symbols))

for char in range(num_numbers):
    password_list.append(random.choice(numbers))

#print(password_list)

random.shuffle(password_list)

#print(password_list)

password=""
for i in password_list:
    password+=i
print(f"Your final password is : {password}")