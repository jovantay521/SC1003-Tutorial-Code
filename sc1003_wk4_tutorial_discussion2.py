# requirements:
# 1. at least 10 characters
# 2. >=5 unique characters
# 3. Must contain uppercase, lowercase and special characters

from string import whitespace


def whitespace_check(password):
    """check for whitespace in password"""
    if ' ' in password:
        return False
    else:
        return True

def password_length_check(password):
    """checks length of passwords"""
    if len(password) >= 10:
        return True
    else:
        return False

def unique_char_check(password):
    """checks for minimum 5 unique characters"""
    newlst = list(set(list(password))) # converts it to a set which removes duplicates
    if len(newlst) >= 5:
        return True
    else:
        return False

def upper_lower_special_char_check(password):
    """check for uppercase, lowercase and special characters"""
    special_char = list("~!@#$%^*-_=+[{]}/;:,.?")

    if any(letter.isupper for letter in password):
        if any(letter.islower for letter in password):
            if any(letter in special_char for letter in password):
                return True
    
    else:
        return False

def main():
    while True:
        new_password = input("Please input your new password here: ")
        if whitespace_check(new_password):
            if password_length_check(new_password):
                if unique_char_check(new_password):
                    if upper_lower_special_char_check(new_password):
                        print(f"Your new password {new_password} has been set. Have a nice day!")
                        quit()
                    else:
                        print("Password must contain at least 1 uppercase, 1 lowercase and 1 special character. Please try again")
                else:
                    print("Password must have at least 5 unique characters. Please Try again.")

            else:
                print("Password must be at least 10 characters. Please try again.")
        
        else:
            print("Whitespace not accepted in password. Please try again.")


if __name__ == "__main__":
    main()