import pytest


class TestFunc:
    def test_add(self):
        assert add(2, 3) == 5

    def test_add(self):
        assert add(3, 3) == 5

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


def add(a, b):
    return a + b
