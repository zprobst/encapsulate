import pytest

from encapsulate.protected import _correctness_check

from .fake_types import Bar, FancyBar, FancyFoo, FancyFooBar, Foo


def test_same_class_passes():
    assert _correctness_check(Foo, Foo)


def test_child_class_passes():
    assert _correctness_check(Foo, FancyFoo)
    assert _correctness_check(Foo, FancyFooBar)


@pytest.mark.parametrize("other_class", [Bar, FancyBar])
def test_other_classes_fail(other_class):
    assert not _correctness_check(Foo, other_class)
