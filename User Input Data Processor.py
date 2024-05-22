#Write a script that checks the length of the user's first name and last name. 
#Both should be at least 2 characters long.
#If not, print an error message.
def user_input():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    if len(first_name) <= 2 or len(last_name) <= 2:
        print("Error. Not a valid user info!")
    
    num_first = len(first_name)
    num_last = len(last_name)
    
    return num_first, num_last

first_len, last_len = user_input()
print(f"First name length: {first_len}, Last name length: {last_len}")
#Create a function that checks the complexity of a user's password. 
# The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number.
# If the password does not meet these criteria, print a message explaining the complexity requirements.
def check_password():
    user_password = input("Enter your password: ")
    if len(user_password) < 8:
        print("Error: Password must be at least 8 characters long.")
        return
    char_upper = False
    char_lower = False
    char_num = False
    for character in user_password:
        if character.isupper():
            char_upper = True
        elif character.islower():
            char_lower = True
        elif character.isdigit():
            char_num = True
    if char_upper and char_lower and char_num:
         print("Valid password!")
    else:
         print("Error: Password must contain at least one uppercase letter, one lowercase letter, and one digit.")

check_password()
#Implement a script that ensures all user email addresses are in a standard format
def email_formatter():
    user_email = input("Enter your email address: ").strip()

    if '@' in user_email and '.' in user_email.split('@')[1]:
        standardized_email = user_email.lower()
        print(f"Enter email: {standardized_email}")
    else:
        print("Error: Invalid email address format.")

email_formatter()