from data.models.User import User


class Users:
    VALID = User("standard_user", "secret_sauce")
    LOCKED = User("locked_out_user", "secret_sauce")
    WRONG_PASSWORD = User("standard_user", "wrong_pass")
    WRONG_USERNAME = User("wrong_user", "secret_sauce")
    EMPTY_USERNAME = User("", "secret_sauce")
    EMPTY_PASSWORD = User("standard_user", "")
