import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
 
  # Define character sets based on user choices
  characters = ""
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_lowercase:
    characters += string.ascii_lowercase
  if include_digits:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation

  # Ensure at least one character from each chosen category if specified
  if not characters:
    raise ValueError("You must choose at least one character type (uppercase, lowercase, digits, or symbols).")
  minLength = 1
  if include_uppercase: minLength += 1
  if include_lowercase: minLength += 1
  if include_digits: minLength += 1
  if include_symbols: minLength += 1
  if length < minLength:
    raise ValueError(f"Password length must be at least {minLength} to include all chosen character types.")

  # Generate random password from chosen character set
  password = "".join(random.choice(characters) for i in range(length))
  return password

# Get user input for password length and complexity
try:
  length = int(input("Enter desired password length: "))
  include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
  include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
  include_digits = input("Include digits? (y/n): ").lower() == "y"
  include_symbols = input("Include symbols? (y/n): ").lower() == "y"
except ValueError:
  print("Invalid input. Please enter a number for password length.")
  exit()

# Generate and display password
try:
  password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
  print(f"Your generated password is: {password}")
except ValueError as e:
  print(e)
