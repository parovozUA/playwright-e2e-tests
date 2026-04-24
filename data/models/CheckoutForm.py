from dataclasses import dataclass


@dataclass
class CheckoutForm:
    first_name: str
    last_name: str
    postal_code: str
