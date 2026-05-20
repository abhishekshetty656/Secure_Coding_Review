# Secure Login System

import hashlib

# Stored username
stored_username = "admin"

# Store hashed password
stored_password = hashlib.sha256("admin123".encode()).hexdigest()

# User input
username = input("Enter Username: ")
password = input("Enter Password: ")

# Convert entered password into hash
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Authentication
if username == stored_username and hashed_password == stored_password:
    print("\nSecure Login Successful")
else:
    print("\nInvalid Credentials")