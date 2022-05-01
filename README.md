# Encapsulate

Coming from a language like ruby, java, or c# where objects can protect their properties? Well, now you can in Python too!

## Getting Started

`pip install encapsulate`

## Usage

### `private` functions

`private` only allows a call to a method to be called from the same class that the
method is a part of.

```python
from encapsulate import private

class MyClass:
    @private
    def foo(self, x, y):
        return x + y

    def bar(self, x, y):
        return self.foo(x, y) + 1   # Allowed

    def other_instances(self, x, y):
        MyClass().foo(x, y )        # Allowed


def outside():
    MyClass().foo(2, 4)             # AttributeError


class OtherClass:
    def test(self):
        MyClass().foo(1, 2)         # AttributeError


MyClass().foo(1, 2)                 # AttributeError
```

### `protected` functions

For all intents and purposes `protected` and `private` are the same save one condition. `protected` alos allows subclasses to access the decorated function.

```python
from encapsulate import protected

class MyClass:
    @protected
    def test(self, x, y):
        pass


class MyBetterClass(MyClass):
    def something_else(self, x, y):
        self.test(x, y) # Allowed
```
