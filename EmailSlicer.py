#collect email addresses from a user 
#split the email using the '@' symbol
#and print the username and domain separately
# import the regular expression module

def email_slicer(email):
    email= input("Enter your email address: ")
    # check if the email address is valid
    if "@" not in email or "." not in email.split("@")[1]:
        return "Invalid email address"  
    

    # split the email address into username and domain

    username, domain = email.split("@")
    # return the username and domain as a tuple
    return username, domain

# Example usage
if __name__ == "__main__":
    email = input("Enter your email address: ")
    username, domain = email_slicer(email)
    print(f"Username: {username}")
    print(f"Domain: {domain}")
