# Secure Coding Review

## Project Overview

This project demonstrates a Secure Coding Review of a Python-based login authentication system. The main objective of this project is to identify security vulnerabilities in an insecure login application and implement secure coding techniques to improve authentication security.

The project includes both a vulnerable login system and a secure login system using password hashing with SHA-256.

---

# Objectives

* Perform secure code review
* Identify security vulnerabilities
* Understand authentication security risks
* Implement secure coding practices
* Improve password protection using hashing

---

# Technologies Used

* Python
* VS Code
* hashlib Library
* GitHub

---

# Project Structure

```text id="rm1"
Secure_Coding_Review/
│
├── vulnerable.py
├── secure_login.py
├── screenshots/
├── report.pdf
└── README.md
```

---

# Vulnerable Login System

The vulnerable login system stores usernames and passwords directly inside the source code using plain text authentication.

## Vulnerabilities Identified

* Hardcoded credentials
* Plain text password storage
* Weak authentication mechanism
* Lack of input validation

## Risk Level

| Vulnerability         | Risk Level |
| --------------------- | ---------- |
| Hardcoded Credentials | High       |
| Plain Text Password   | High       |
| Weak Authentication   | Medium     |
| No Input Validation   | Medium     |

---

# Secure Login System

The secure login system improves authentication security by implementing SHA-256 password hashing using Python’s hashlib module.

## Security Improvements

* Password hashing using SHA-256
* Better password protection
* Improved authentication mechanism
* Secure coding practices

---

# Sample Secure Code

```python id="rm2"
import hashlib

stored_username = "admin"

stored_password = hashlib.sha256("admin123".encode()).hexdigest()

username = input("Enter Username: ")
password = input("Enter Password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

if username == stored_username and hashed_password == stored_password:
    print("Secure Login Successful")
else:
    print("Invalid Credentials")
```

---

# Learning Outcome

Through this project, I learned about:

* Secure coding principles
* Password hashing
* Authentication security
* Vulnerability analysis
* Cybersecurity best practices

---

# Conclusion

This project demonstrates the importance of secure coding practices in protecting applications from cyber threats and unauthorized access. By implementing password hashing and improving authentication mechanisms, the security of the login system was significantly enhanced.

---

# References

* Python Official Documentation
* OWASP Secure Coding Practices
* hashlib Documentation

---

# Author

Abhishek
