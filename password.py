import random
import string

def generate_password(length: int) -> str:
    if length < 1:
        return "Password length must be at least 1."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    
    return password

try:
    length = int(input("Enter the desired password length: "))
    print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")


