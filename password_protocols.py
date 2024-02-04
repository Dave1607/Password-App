import string
import random

#check for password that are strong
def valid_password(password):
    special_characters = string.punctuation
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digit = string.digits

    if len(password) >= 8:
        if any(character in upper_case for character in password):
            if any(character in lower_case for character in password):
                if  any(character in special_characters for character in password) or any(character in digit for character in password):
                    return {
                        "strenght": "strong",
                        "valid": True,
                        "comment": "Password meets the criteria.",
                        }
                else:
                    return {
                        "strenght": "weak",
                        "valid": False,
                        "comment": "Password should contain at least one special character or Number.",
                        }
            else:
                return {
                        "strenght": "weak",
                        "valid": False,
                        "comment": "Password should contain at least one lowercase letter.",
                        }
        else:
            return {
                    "strenght": "weak",
                    "valid": False,
                    "comment": "Password should contain at least one uppercase letter.",
                    }
    else:
        return {
                "strenght": "weak",
                "valid": False,
                "comment": "Password should be at least 8 characters long.",
                }

#function to generate password following  given conditions for a strong password
def generate_password():
    lowercase = ''.join(random.choices(string.ascii_lowercase, k=random.choice(range(4,7))))
    uppercase = ''.join(random.choices(string.ascii_uppercase, k=random.choice(range(2,3))))
    special_characters = ''.join(random.choices(string.punctuation, k=random.choice(range(1,3))))
    digits = ''.join(random.choices(string.digits, k=random.choice(range(1,3))))

    password = list(lowercase + uppercase + special_characters + digits)
    random.shuffle(password)

    return ''.join(password)