# Hey today i am going to learn data visualisation
print("Hey today i am going to learn data visualisation")

# Now i am changing this file
import random
import string

def generate_password(length=12):
    """Generate a random password with uppercase letters, lowercase letters, digits, and punctuation."""
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password contains at least one of each character type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(characters, k=length - 4)
    
    # Shuffle the list to ensure a random order
    random.shuffle(password)
    
    # Join the list into a string and return it
    return "".join(password)

# Generate and print a random password
new_password = generate_password()
print(f"Your new random password is: {new_password}")
