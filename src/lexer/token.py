from typing import Optional


class Token:
    """
    This class creates a structure to represent a token.
    It's necessary to give the name (id of this token) and its value.
    Information such as type, line and column are optional.
    """

    def __init__(
        self,
        value: str,
        token_type: Optional[str] = None,
        line: Optional[int] = None,
        column: Optional[int] = None,
    ) -> None:
        self.value = value
        self.token_type: Optional[str] = token_type
        self.line: Optional[int] = line
        self.column: Optional[int] = column

    def __str__(self) -> str:
        return f"Token({self.value}, {self.token_type})"
