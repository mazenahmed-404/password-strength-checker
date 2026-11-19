# Main Function
def main():

    # Usage Manual to the User
    print("---------------------------------------") # Just a UI Separator
    print(" Welcome to Password Strength Checker!")
    print("---------------------------------------")
    print("Include in your password:\n1. Uppercases \n2. lowercases  \n3.special characters \n4.numbers \n5.make it at least 8 characters! ")
    print("---------------------------------------")
    print("We will rate you password as one of these: \n1. Very Strong \n2. Strong  \n3.Moderate \n4.Weak \n5.Very weak ")
    print("---------------------------------------")
    print("#######################################")
    print("If you wish to terminate the program, jsut type \"x\" in the password section ")

    # Requesting password from the user
    password = input("Enter your password here: ")

    # Evaluating the entered password
    while password.lower() !="x": # Iterates the program till terminated by the user
        length = get_length(password)
        uppercase = check_upper(password)
        lowercase = check_lower(password)
        special = check_special(password)
        number = check_number(password)
        score = length + uppercase + lowercase + special + number
        if score == 5:
            print("Your password is Very Strong!")
        elif score == 4:
            print("Your password is Strong!")
        elif score == 3:
            print("Your password is Moderate!")
        elif score == 2:
            print("Your password is Weak!")
        elif score == 1:
            print("Your password is Very Weak!")
        elif score == 0:
            print("Please Enter a password buddy!")
        
        print("---------------------------------------")        
        # Find where the problem is exactly
        lack_length(length)
        lack_lowercase(lowercase)
        lack_special(special)
        lack_uppercase(uppercase)
        lack_number(number)
        print("---------------------------------------")

        # Requesting a new password
        password = input("Enter your password here: ")

# Calculating the length of the password
def get_length(passwd):
    length = len(passwd)
    if length >= 8:
        return 1
    else:
        return 0

# Making sure the password contains an Uppercase letter   
def check_upper(passwd):
    for letter in passwd:
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": # you can use .isupper()
            return 1
    return 0

# Making sure the password contains a Lowercase letter   
def check_lower(passwd):
    for letter in passwd:
        if letter in "abcdefghijklmnopqrstuvwxyz": # you can use .islower()
            return 1
    return 0

# Making sure the password contains a special character 
def check_special(passwd):
    for letter in passwd:
        if letter in "!@#$%^&*()_+-={}[]|\';:\"/.,<>?":
            return 1
    return 0

# Making sure the password contains a number
def check_number(passwd):
    for letter in passwd:
        if letter in "1234567890": # you can use .isdigit()
            return 1
    return 0

# Getting where the problem is and showing it to the user

# If the password lacks an Uppercase letter
def lack_uppercase(upper):
    if upper == 0:
        print("Please, include an uppercase letter in your password!")


# If the password lacks a Lowercase letter    
def lack_lowercase(lower):
    if lower == 0:
        print("Please, include a lowercase letter in your password!")


# If the password lacks a special character     
def lack_special(special):
    if special == 0:
        print("Please, include a special character in your password!")


# If the password lacks a number     
def lack_number(number):
    if number == 0:
        print("Please, include a number in your password!")


# If the password is less than 8 characters    
def lack_length(TheLength):
    if TheLength == 0:
        print("Please, make your password at least 8 charcters!")

    

main()
