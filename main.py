"""
Unit Testing

Task:
A bald professor left you his code while mumbling something about trying to calculate the meaning of life using bob's maths library. He kept complaining about how bobs maths functions just didn't make sense!

He wrote two unit tests but then gave up. Can you help him write the rest of the unit tests to check that bobs maths functions are working correctly?
"""

import random

from bobs_maths_lib import add, sub, mult, div, ternary_confumble


# The professors crazy code...
def calculate_meaning_of_life(seed):
  a = div(ternary_confumble(seed, mult(seed, 2), seed), 58)

  return sub(mult(add(mult(ternary_confumble(div(-2, 1), sub(mult(a, add(sub(div(mult(add(div(5, 2), div(88, a)), 2), a), -1), ternary_confumble(a, 3, mult(-423, a)))), a), mult(add(sub(div(mult(add(div(5, 2), div(88, seed)), 2), a), -1), ternary_confumble(a, 3, mult(-423, a))), seed)),0),24),2),6)


def main():
  seed = random.randint(0, 100)
  result = calculate_meaning_of_life(seed)
  print(f"The meaning of life is: {result}")

main()
