from dataclasses import dataclass


@dataclass(kw_only=True)
class BaseCase:
    name: str
    should_pass: bool
    xfail_reason: str | None = None
    error_message: str | None = None

    # validate that error_message is set if should_pass is False
    def __post_init__(self):
        if not self.should_pass and self.error_message is None:
            raise ValueError(f"{self.name}: error_message is required")

    def __str__(self):
        return self.name