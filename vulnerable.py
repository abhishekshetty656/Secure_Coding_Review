# Vulnerable Login System

username = input("Enter Username: ")
password = input("Enter Password: ")

# Hardcoded credentials (Vulnerability)
if username == "admin" and password == "admin123":
    print("\nLogin Successful")
else:
    print("\nInvalid Credentials")