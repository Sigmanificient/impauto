"""A python package to handle automatically input for faster development."""
import builtins

from typing import Callable, Optional, Generator, Tuple

author: str = "Sigmanificient"
version: str = "1.0.1"


class Automated:

    def __init__(self, *args, show_message: bool = True, forever: bool = False) -> None:
        """Create a value generator and replace the builtin input."""
        self.values: Generator = self.__generate_values(args, forever)
        self.show_message: bool = show_message

        builtins.input: Callable[[Optional[str]], str] = self.__input__

    @staticmethod
    def __generate_values(values, forever: bool) -> Generator:
        values: Tuple[str] = tuple(map(str, values))
        once: int = 1

        while forever or once:
            yield from values
            once: int = 0

        raise StopIteration("No more input values given. Make sure to have enough values passed")

    def __input__(self, __prompt: Optional[str] = None) -> str:
        """Method that will replace the builtin input."""
        value: str = next(self.values)

        if self.show_message:
            print(f"[Automated] {__prompt}{value}")

        return str(value)
