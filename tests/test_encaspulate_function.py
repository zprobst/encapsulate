from unittest.mock import MagicMock

import pytest

from encapsulate.encapsulate_function import encapsulate_function


def test_encapsulate_function_failing_case():
    correctness_check = MagicMock(return_value=False)

    class MyProtectedClass:
        def test(self):
            pass

        test = encapsulate_function(test, correctness_check)

    with pytest.raises(AttributeError):
        instance = MyProtectedClass()
        instance.test()


def test_encapsulate_function_passing_case():
    correctness_check = MagicMock(return_value=True)
    original_function = MagicMock()

    class MyProtectedClass:
        test = original_function
        test = encapsulate_function(test, correctness_check)

    instance = MyProtectedClass()
    instance.test(1, 2, foo="bar")

    original_function.assert_called_once_with(instance, 1, 2, foo="bar")


def test_infers_caller_correctly():
    correctness_check = MagicMock(return_value=True)
    original_function = MagicMock()

    class ProtectedClass:
        test = original_function
        test = encapsulate_function(test, correctness_check)

    class OtherClass:
        def do_something_with_protected(self, protected):
            protected.test()

    OtherClass().do_something_with_protected(ProtectedClass())

    correctness_check.assert_called_once_with(ProtectedClass, OtherClass)
