from lexer.code_handler import CodeHandler
from lexer.lexer import Lexer
import asyncio


async def main():
    handler = CodeHandler()
    source_code = await handler.read_code_file("program.xqdl")

    lexer = Lexer()
    try:
        tokens = lexer.tokenize(source_code)
        for token in tokens:
            print(token.__str__())
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())
