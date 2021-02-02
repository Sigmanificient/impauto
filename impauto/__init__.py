import builtins

author = "Edhyjox"
version = "1.0.0"


class automated:

    def __init__(self, *args, show_message=True, forever=False):
        self.values = self.__generate_values(args) if forever else iter(args)
        self.show_message = show_message

        builtins.input = self.__input__

    @staticmethod
    def __generate_values(values):
        values = map(str, values)
        while True:
            for value in values:
                yield str(value)

    def __input__(self, __prompt=None):
        value = next(self.values)
        if self.show_message:
            print(f"[Automated] {__prompt}{value}")
        return str(value)