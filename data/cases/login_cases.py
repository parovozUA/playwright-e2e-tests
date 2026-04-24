from data.models.User import Users

LOGIN_CASES = [
    LoginCase(
        name="valid user",
        user=Users.VALID,
        should_pass=True
    ),
    LoginCase(
        name="wrong username",
        user=Users.WRONG_USERNAME,
        should_pass=False,
        error_message="Username and password do not match"
    ),
    LoginCase(
        name="wrong password",
        user=Users.WRONG_PASSWORD,
        should_pass=False,
        error_message="Username and password do not match"
    ),
    LoginCase(
        name="empty username",
        user=Users.EMPTY_USERNAME,
        should_pass=False,
        error_message="Username is required"
    ),
    LoginCase(
        name="empty password",
        user=Users.EMPTY_PASSWORD,
        should_pass=False,
        error_message="Password is required"
    ),
    LoginCase(
        name="locked user",
        user=Users.LOCKED,
        should_pass=False,
        error_message="Sorry, this user has been locked out"
    ),
]
