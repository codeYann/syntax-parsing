from typing import List
from lexer.token import Token
from lexer.code_handler import CodeHandler
from lexer.lexer import Lexer, LexicalError
from parser.parser import Parser, SyntacticalError
import asyncio


async def main():
    handler = CodeHandler()
    lexer = Lexer()
    source_code = await handler.read_code_file("program.xqdl")
    tokens: List[Token] = []

    try:
        tokens = lexer.tokenize(source_code)
    except LexicalError as e:
        print(e)
        return

    parser = Parser(tokens)
    try:
        parser.parse()
    except SyntacticalError as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())
