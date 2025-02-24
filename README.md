# PASSWORD-GENERATOR

This Python script generates a random password of user-specified length using uppercase letters, lowercase letters, digits, and special characters. 
Imports random and string modules to access characters and generate random selections.
Defines generate_password(length) function:
Ensures the length is at least 1.
Combines alphabets, digits, and special characters. 
Uses random.choices() to randomly select characters for the password.
Takes user input for password length and handles invalid inputs using try-except.
Prints the generated password if input is valid.
