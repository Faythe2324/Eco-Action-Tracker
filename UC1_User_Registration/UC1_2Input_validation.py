"""
Validates registration fields before account creation.
"""

class InputValidator:
    def validate(self, username, email, password, confirm_password):
        if len(username) < 3:
            return "Username must have at least 3 characters."
        if "@" not in email:
            return "Enter a valid email address."
    
        return "Input valid."

if __name__ == "__main__":
    v = InputValidator()
    print(v.validate("Abi", "abi@mail.com", "123456", "123456"))
