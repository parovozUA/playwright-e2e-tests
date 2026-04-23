from dataclasses import dataclass
from data.Users import User

from data.Users import Users


@dataclass
class LoginCase:
    name: str
    user: User
    should_pass: bool
    error_message: str | None = None


LOGIN_CASES = [
    LoginCase(
        "valid user",
        user=Users.VALID,
        should_pass=True
    ),
    LoginCase(
        "wrong username",
        user=Users.WRONG_USERNAME,
        should_pass=False,
        error_message="Username and password do not match"
    ),
    LoginCase(
        "wrong password",
        user=Users.WRONG_PASSWORD,
        should_pass=False,
        error_message="Username and password do not match"
    ),
    LoginCase(
        "empty username",
        user=Users.EMPTY_USERNAME,
        should_pass=False,
        error_message="Username is required"
    ),
    LoginCase(
        "empty password",
        user=Users.EMPTY_PASSWORD,
        should_pass=False,
        error_message="Password is required"
    ),
    LoginCase(
        "locked user",
        user=Users.LOCKED,
        should_pass=False,
        error_message="Sorry, this user has been locked out"
    ),
]
