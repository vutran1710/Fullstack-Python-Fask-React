from string import ascii_lowercase, digits
from random import choice, randrange


class DataGenerator:
    types = ["str", "real", "int", "alpha_numeric"]

    def random_str(self, length=10) -> str:
        letters = [choice(ascii_lowercase) for i in range(length)]
        return "".join(letters)

    def random_real(self) -> float:
        rand_float = randrange(1000, 10000) / 100
        return rand_float

    def random_int(self) -> int:
        rand_int = randrange(1, 10000)
        return rand_int

    def random_alpha_numeric(self, length=10) -> str:
        def gen(i: int):
            return choice(digits if i % 2 == 0 else ascii_lowercase)

        chars = list(map(gen, range(length)))
        return "".join(chars)

    def generate_randoms(self, suffix=None, hook=None) -> str:
        """Generator to produce a random
        stringified value from defined data-types
        """
        while True:
            data_type = choice(self.types)
            method = "random_" + data_type
            value = getattr(self, method)()

            if callable(hook):
                hook(value, data_type)

            yield str(value) + (suffix or "")
