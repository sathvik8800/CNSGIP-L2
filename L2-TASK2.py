def check_password_strength(password):
   
    length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/`~' for c in password)
    
    if all([length, has_upper, has_lower, has_digit, has_special]):
        return "Password is strong."
    else:
        return "Password is weak."

input_password = input("Enter a password to check its strength: ")

result = check_password_strength(input_password)


print(result)
