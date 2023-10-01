# Imports
import random

print("Welcome to the PyPass Generator!")

# Configuration
l_list = "abcdefghijklmnopqrstuvwxyz"
s_list = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"
n_list = "0123456789"

password = ""
password_list = []

# Collect user input
letters = int(input("\nHow many letters would you like in your password: "))
symbols = int(input("How many symbols would you like: "))
numbers = int(input("How many numbers would you like: "))

# Generation
for char in range(letters):
    l_char = random.choice(l_list)
    password_list.append(l_char)
    password += l_char

for symb in range(symbols):
    s_char = random.choice(s_list)
    password_list.append(s_char)
    password += s_char

for num in range(numbers):
    n_char = random.choice(n_list)
    password_list.append(n_char)
    password += n_char

# Shuffles to increase 'randomness' then returns
random.shuffle(password_list)
password = ''.join(password_list)
print("\nYour password is:", password)