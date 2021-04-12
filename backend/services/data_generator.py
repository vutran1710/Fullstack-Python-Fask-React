from string import ascii_lowercase, digits
from random import choice, randrange, sample


class DataGenerator:
    def __init__(self):
        pass

    def random_str(self, length=10) -> str:
        letters = [choice(ascii_lowercase) for i in range(length)]
        return "".join(letters)

    def random_real(self) -> float:
        rand_float = randrange(0, 10000) / 100
        return rand_float

    def random_int(self) -> int:
        rand_int = randrange(1, 10000)
        return rand_int

    def random_alpha_numeric(self, length=10) -> str:
        def _gen_(i: int):
            return choice(digits if i % 2 == 0 else ascii_lowercase)

        chars = list(map(_gen_, range(length)))
        return "".join(chars)
