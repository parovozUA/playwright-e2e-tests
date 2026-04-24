from dataclasses import dataclass

from data.models.BaseCase import BaseCase
from data.models.User import User


@dataclass
class LoginCase(BaseCase):
    user: User
