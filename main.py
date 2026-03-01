from pyscript import document #type: ignore

# utilities for password validation

def contains_letter(s: str) -> bool:
    """Return True if there is at least one alphabetic character."""
    return any(c.isalpha() for c in s)


def contains_number(s: str) -> bool:
    """Return True if there is at least one digit."""
    return any(c.isdigit() for c in s)


def account_creation(e=None):
    # read current values
    username = document.getElementById("username").value or ""
    password = document.getElementById("password").value or ""

    username_len = len(username)
    password_len = len(password)

    # reset any prior messages
    document.getElementById("username-error").innerHTML = ""
    document.getElementById("password-error").innerHTML = ""
    document.getElementById("output").innerHTML = ""

    # accumulate errors consistently for each field
    user_errors = []
    pass_errors = []

    # immediate click without typing anything
    if username_len == 0:
        user_errors.append("Please enter a username.")
    elif username_len < 7:
        user_errors.append(f"Username must be at least 7 characters long. Add {7 - username_len} more.")

    if password_len == 0:
        pass_errors.append("Please enter a password.")
    else:
        if password_len < 10:
            pass_errors.append(f"Password must be at least 10 characters long. Add {10 - password_len} more.")
        if not contains_letter(password):
            pass_errors.append("Password must include a letter.")
        if not contains_number(password):
            pass_errors.append("Password must include a number.")

    # display errors if any
    if user_errors:
        document.getElementById("username-error").innerHTML = "<br>".join(user_errors)
    if pass_errors:
        document.getElementById("password-error").innerHTML = "<br>".join(pass_errors)

    # success message if all requirements satisfied
    if not user_errors and not pass_errors:
        document.getElementById("output").innerHTML = "Account created successfully!"


