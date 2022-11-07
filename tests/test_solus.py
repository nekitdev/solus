from solus import Singleton, UnsafeSingleton


class UnsafeNull(UnsafeSingleton):
    pass


UNSAFE_NULL = UnsafeNull()


def test_unsafe_singleton() -> None:
    assert UnsafeNull() is UNSAFE_NULL


class Null(Singleton):
    pass


NULL = Null()


def test_singleton() -> None:
    assert Null() is NULL
