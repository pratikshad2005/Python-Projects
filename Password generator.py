# This project helps you learn how to build a customizable password generator that creates secure passwords using different character types. 
# It allows users to choose:

import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if characters == "":
        return "No character set selected"

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


# Take password length input (minimum 6 required)
length = int(input("Enter password length (minimum 6): "))

# Ask user for choices (yes/no)
use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
use_digits = input("Include numbers? (yes/no): ").lower() == "yes"
use_special = input("Include special characters? (yes/no): ").lower() == "yes"

# Validate minimum length
if length < 6:
    print("Password length must be at least 6")
else:
    # Call generate_password function
    password = generate_password(
        length, use_uppercase, use_lowercase, use_digits, use_special
    )
    print("Generated Password:", password)

