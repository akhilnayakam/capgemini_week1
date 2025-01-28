def check_password_strength(password):
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lower = "qwertyuiopasdfghjklzxcvbnm"
    digit = "1234567890"
    special = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"

    has_upper = has_lower = has_digit = has_special = False

    for char in password:
        if char in upper:
            has_upper = True
        elif char in lower:
            has_lower = True
        elif char in digit:
            has_digit = True
        elif char in special:
            has_special = True

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong Password"
    else:
        reasons = []
        if len(password) < 8:
            reasons.append("must be at least 8 characters long")
        if not has_upper:
            reasons.append("must include at least one uppercase letter")
        if not has_lower:
            reasons.append("must include at least one lowercase letter")
        if not has_digit:
            reasons.append("must include at least one digit")
        if not has_special:
            reasons.append("must include at least one special character")
        return "Weak Password: " + ", ".join(reasons)

def main():
    password = input("Enter your password: ")
    print(check_password_strength(password))

main()
