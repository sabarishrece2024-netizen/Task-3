import random
import string

# Minimum length check
length = int(input("Enter password length (min 8): "))

if length < 8:
    print("Password length must be at least 8")
else:
    # Required characters
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    # Remaining characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = length - 4

    password = upper + lower + digit + symbol
    for i in range(remaining):
        password += random.choice(all_chars)

    # Shuffle password
    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)

    print("Strong Password:", password)