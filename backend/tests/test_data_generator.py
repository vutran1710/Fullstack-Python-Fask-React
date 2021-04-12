from functools import reduce
from services import DataGenerator

dg = DataGenerator()


def test_random_string():
    random_str = dg.random_str()
    print(random_str)
    assert len(random_str) == 10

    for char in random_str:
        assert not char.isdigit()

    random_str = dg.random_str(length=20)
    print(random_str)
    assert len(random_str) == 20


def test_real_number():
    random_real = dg.random_real()
    print(random_real)
    assert isinstance(random_real, float)


def test_integer():
    random_int = dg.random_int()
    print(random_int)
    assert isinstance(random_int, int)


def test_alpha_numberic():
    random_an = dg.random_alpha_numeric()
    print(random_an)
    assert random_an.isalnum()


def test_random_any():
    gen = dg.generate_randoms(suffix=",")

    for _ in range(10):
        print(next(gen))
