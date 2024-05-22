#Write a script that takes a user's text input and identifies if it contains one of the predefined commands
# (e.g., "help", "issue", "contact support"). 
#If a command is found, print a response related to the command.
def category():
    user_input = input("Enter the text: ")
    predefined_words = ["help", "issue", "contact support"] 
    issue_keywords = {
        "login": ["login", "sign in", "log in", "authentication"],
        "performance": ["slow", "lag", "performance", "speed"],
        "error": ["error", "bug", "crash", "failure"]
    }
    
    for predefined_word in predefined_words:
        if predefined_word in user_input:
            print(f"The command '{predefined_word}' is found")
# If the user's input contains the word "issue", further categorize the issue based on keywords
# such as "login", "performance", "error", etc. 
# Print out the category of the issue for the support team.
            if predefined_word == "issue":
                categorized = False
                for category, keywords in issue_keywords.items():
                    for keyword in keywords:
                        if keyword in user_input:
                            print(f"The issue category is '{category}'")
                            categorized = True
                            break
                    if categorized:
                        break
                if not categorized:
                    print("The issue category is 'general'")
                    
category()
