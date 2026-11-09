import random
import string

# Functoin to generate a random password based on user criteria 
def generate_password(min_length, numbers=True, special_characters=True ):
    # Prepare standard character sets
    letters = string.ascii_letters      # Contains a-z and A-Z
    digits = string.digits              # Contains 0-9
    special = string.punctuation        # Contains symbols like !,@,#,& etc.

    # Start the pool with letters,then add requested character types
    characters = letters 
    if numbers:
        characters += digits            # Add numbers if requested
    if special_characters:
        characters += special           # Add symbols if requested

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    # Keep adding characters until the password is long enough AND contains required types
    while not meets_criteria or len(pwd) < min_length:
        # Pick one random character from our allowed pool and attach it to the password
        new_char = random.choice(characters)
        pwd += new_char

        # Track if the newly added character is a digit or symbol
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # Verify whether all selected user rules are satisfied 
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    # Return the completed password to the caller
    return pwd 

# --- Main Program Execution ---

# Get minimum password length from user and convert input to an integer 
min_length = int(input("Enter the minimum length: "))

# Ask user options and convert 'y' responses to True (or False if 'n')
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

# Generate password using user's selected preferences
pwd = generate_password(min_length, has_number, has_special)

# Display the generated password
print("The generated password is:" ,pwd)