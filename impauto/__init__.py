import builtins

author = "Edhyjox"
version = "1.0.1"


class Automated:

    def __init__(self, *args, show_message=True, forever=False):
        self.values = self.__generate_values(args, forever)
        self.show_message = show_message

        builtins.input = self.__input__

    @staticmethod
    def __generate_values(values, forever):
        values = map(str, values)
        once = 1

        while forever or once:
            once -= 1

            for value in values:
                yield value
        raise StopIteration("No more input values given. Make sure to have enough values passed")

    def __input__(self, __prompt=None):
        value = next(self.values)
        if self.show_message:
            print(f"[Automated] {__prompt}{value}")
        return str(value)
