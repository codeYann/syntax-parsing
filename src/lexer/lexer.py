from typing import Callable, List, Dict
from .token import Token
from toolz import pipe
import re


class LexicalError(Exception):
    pass


class Lexer:
    patterns: Dict[str, str] = {
        r"not\b": "NOT_OP",
        r"div\b": "MUL_OP",
        r"or|and|=|<>|<=|>=|<|>": "RELATIONAL_OP",
        r"[a-zA-Z][a-zA-Z0-9]*": "IDENTIFIER",
        r":=": "ASSIGNMENT",
        r"\+|-": "ADD_OP",
        r"\*": "MUL_OP",
        r"\d+": "DIGIT",
        r"\(": "LPAREN",
        r"\)": "RPAREN",
    }

    def remove_newlines_and_spaces(self, code: str) -> str:
        remove_newlines: Callable[[str], str] = lambda s: s.replace("\n", "")
        remove_spaces: Callable[[str], str] = lambda s: s.replace(" ", "")
        return pipe(code, remove_newlines, remove_spaces)

    def tokenize(self, code: str) -> List[Token]:
        code = self.remove_newlines_and_spaces(code)
        remaining_code = code
        tokens: List[Token] = []

        while remaining_code:
            match, token_type = None, None
            longest_match = 0

            for pattern, pattern_desc in self.patterns.items():
                regex = re.compile(pattern)
                found_match = regex.match(remaining_code)

                if found_match:
                    match_length = found_match.end()
                    if match_length > longest_match:
                        match = found_match
                        longest_match = match_length
                        token_type = pattern_desc
            if match:
                value = match.group()
                token = Token(value, token_type)
                tokens.append(token)
                remaining_code = remaining_code[longest_match:].lstrip()
            else:
                raise LexicalError(
                    f"Lexical Error. Unrecognized input {remaining_code[0]}"
                )

        return tokens
