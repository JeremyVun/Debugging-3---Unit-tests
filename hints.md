# Hints
# Hint 1
Sometimes code is really just too complicated to read. Instead of trying to understand the code to debug it, it's better to give up and just write a unit test for each smaller function.

When you write a unit test, you don't care how the function does what it does, you only care that it returns the correct output when you give it a certain input

e.g. a python unit test that tests a a subtract(a, b) function 999999 times with random numbers
```
import unittest

class TestClass:
  def test_my_subtract_function:
    for i in range(99999):
      a = random.randint(-1000, 1000)
      b = random.randint(-1000, 1000)

      expected = a - b
      actual = subtract(a, b)

      self.assertEquals(actual, expected)
```