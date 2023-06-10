from typing import List
from lexer.token import Token

EMPTY_TOKEN = Token("EMPTY", "EMPTY")


class SyntacticalError(Exception):
    pass


class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = tokens
        self.token_index = 0
        self.current_token = self.tokens[0] if len(self.tokens) > 0 else EMPTY_TOKEN

    def move_forward(self) -> None:
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = EMPTY_TOKEN

    def match(self, expected_type: str) -> None:
        if self.current_token.token_type == expected_type:
            self.move_forward()
        else:
            raise SyntaxError(
                f"Syntax Error. Expected {expected_type}, found {self.current_token.token_type}"
            )

    def parse(self) -> None:
        self.parse_assignment_statement()

    def parse_assignment_statement(self) -> None:
        self.parse_identifier()
        self.match("ASSIGNMENT")
        self.parse_expression()

    def parse_expression(self) -> None:
        self.parse_simple_expression()
        self.parse_expression_refactoring()

    def parse_simple_expression(self) -> None:
        if self.current_token.token_type in ["ADD_OP"]:
            self.match("ADD_OP")
        self.parse_term()
        while self.current_token.token_type in ["ADD_OP"]:
            self.match("ADD_OP")
            self.parse_term()

    def parse_term(self) -> None:
        self.parse_factor()

        while self.current_token.token_type in ["MUL_OP"]:
            self.match("MUL_OP")
            self.parse_factor()

    def parse_factor(self) -> None:
        if self.current_token.token_type == "IDENTIFIER":
            self.match("IDENTIFIER")
        elif self.current_token.token_type == "LPAREN":
            self.match("LPAREN")
            self.parse_expression()
            self.match("RPAREN")
        elif self.current_token.token_type == "NOT_OP":
            self.match("NOT_OP")
            self.parse_factor()
        elif self.current_token.token_type == "DIGIT":
            self.match("DIGIT")
        else:
            raise SyntaxError(
                f"Syntax Error. Unexpected token {self.current_token.value}"
            )

    def parse_expression_refactoring(self) -> None:
        if self.current_token.token_type == "RELATIONAL_OP":
            self.match("RELATIONAL_OP")
            self.parse_simple_expression()
        else:
            pass

    def parse_identifier(self) -> None:
        self.match("IDENTIFIER")
