"""
A python package to handle automatically input for faster development.
"""
import builtins

author = "Sigmanificient"
version = "1.0.1"


class Automated:

    def __init__(self, *args, show_message=True, forever=False):
        """Create a value generator and replace the builtin input."""
        self.values = self.__generate_values(args, forever)
        self.show_message = show_message

        builtins.input = self.__input__

    @staticmethod
    def __generate_values(values, forever):
        values = tuple(map(str, values))
        once = 1

        while forever or once:
            yield from values
            once = False

        raise StopIteration("No more input values given. Make sure to have enough values passed")

    def __input__(self, __prompt=None):

        value = next(self.values)

        if self.show_message:
            print(f"[Automated] {__prompt}{value}")

        return str(value)
