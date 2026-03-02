from pyscript import document  # type: ignore


def contains_letter(s: str) -> bool:
    #Return True if ``s`` contains at least one alphabetic character.
    return any(c.isalpha() for c in s)


def contains_number(s: str) -> bool:
    #Return True if ``s`` contains at least one digit.
    return any(c.isdigit() for c in s)


def account_creation(e=None):
    #Validate username/password fields and update the DOM with feedback.

    username = document.getElementById("username").value or ""
    password = document.getElementById("password").value or ""

    # clear any previous messages
    document.getElementById("username-error").innerHTML = ""
    document.getElementById("password-error").innerHTML = ""
    document.getElementById("output").innerHTML = ""

    user_errors: list[str] = []
    pass_errors: list[str] = []

    # username rules
    if not username:
        user_errors.append("Please enter a username.")
    elif len(username) < 7:
        user_errors.append(f"Username must be at least 7 characters long. Add {7 - len(username)} more.")

    # password rules
    if not password:
        pass_errors.append("Please enter a password.")
    else:
        if len(password) < 10:
            pass_errors.append(f"Password must be at least 10 characters long. Add {10 - len(password)} more.")
        if not contains_letter(password):
            pass_errors.append("Password must include at least one letter.")
        if not contains_number(password):
            pass_errors.append("Password must include at least one number.")

    # write errors back to page
    if user_errors:
        document.getElementById("username-error").innerHTML = "<br>".join(user_errors)
    if pass_errors:
        document.getElementById("password-error").innerHTML = "<br>".join(pass_errors)

    if not user_errors and not pass_errors:
        document.getElementById("output").innerHTML = "Account created successfully!"



