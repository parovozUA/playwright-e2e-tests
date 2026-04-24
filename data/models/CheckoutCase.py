from dataclasses import dataclass

from data.models.BaseCase import BaseCase
from data.models.CheckoutForm import CheckoutForm


@dataclass
class CheckoutCase(BaseCase):
    form: CheckoutForm
