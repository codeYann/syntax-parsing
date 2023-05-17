import os
import aiofiles


class CodeHandler:
    """
    CodeHandler class defines methods to handle access to program source code
    in async way.
    """

    def __fix_relative_path(self, file_name: str) -> str:
        """
        __fix_relative_path is a private method which solves the path to
        get program source code.
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, "../source_code/", file_name)

    async def read_code_file(self, file_name: str) -> str:
        """
        read_code_file is a public method that returns the content of program
        source code.
        """
        path = self.__fix_relative_path(file_name)
        try:
            async with aiofiles.open(path, mode="r") as file:
                content = await file.read()
                return content
        except FileNotFoundError:
            print(f"File {path} not found.")
            return ""
