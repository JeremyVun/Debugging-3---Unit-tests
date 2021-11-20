"""
Unit Testing

Task:
A bald professor left you his code while mumbling something about trying to calculate the meaning of life using bob's maths library. He kept complaining about how bobs maths functions just didn't make sense!

He wrote two unit tests but then gave up. Can you help him write the rest of the unit tests to check that bobs maths functions are working correctly?
"""

import random

# Write unit tests to test bob's add, sub, mult, div, and ternary_confumble functions
from bobs_maths_lib import add, sub, mult, div, ternary_confumble


def main():
  seed = random.randint(0, 100)
  result = calculate_meaning_of_life(seed)
  print(f"The meaning of life is: {int(result)}")


# The professors crazy code... don't even try...
def calculate_meaning_of_life(seed):
  a = div(ternary_confumble(seed, mult(seed, 2), seed), 58)

  b = sub(mult(div(ternary_confumble(seed, mult(seed, 2), seed), 58), add(sub(div(mult(add(div(5, 2), div(88, a)), 2), a), -1), ternary_confumble(a, 3, mult(-423, a)))), a)

  c = sub(mult(a, add(sub(div(mult(add(div(5, 2), div(88, sub(mult(add(mult(ternary_confumble(div(-2, 1), sub(mult(a, add(sub(div(mult(add(div(5, b), div(88, a)), 2), a), -1), ternary_confumble(a, 3, mult(-423, a)))), a), mult(add(sub(div(mult(add(div(5, 2), div(88, seed)), b), a), -1), ternary_confumble(a, 3, mult(-423, a))), seed)),0),24),2),6))), 2), a), -1), ternary_confumble(a, seed, mult(-423, a)))), a)

  d = ternary_confumble(a, div(mult(add(div(5, a), div(88, seed)), 2), a), -1)

  return sub(mult(add(mult(ternary_confumble(div(-2, 1), sub(mult(a, add(sub(div(mult(add(div(5, d), div(d, sub(mult(add(mult(ternary_confumble(div(-1 * seed, 1), sub(mult(a, add(sub(div(mult(add(div(5, b), div(seed, sub(mult(add(mult(ternary_confumble(div(-2, 1), sub(mult(a, add(sub(div(mult(add(div(5, c), div(d, a)), 2), a), -1), ternary_confumble(a, 3, mult(-1 * a, a)))), a), mult(add(sub(div(mult(add(div(5, 2), div(c, seed)), b), a), -1), ternary_confumble(a, 3, mult(-1 * b, a))), seed)),0),c),d),6))), 2), a), -1), ternary_confumble(a, seed, mult(-7, a)))), a), mult(add(sub(div(mult(add(div(5, a), div(c, seed)), 2), a), -1), ternary_confumble(a, b, mult(-1 * d, b))), seed)),0),24),2),6))), 2), a), -1), ternary_confumble(a, 3, mult(-423, a)))), a), mult(add(sub(div(mult(add(div(5, 2), div(a, seed)), 2), a), -1), ternary_confumble(a, 3, mult(-12, a))), seed)),0),24),2),6)


if __name__ == "__main__":
  main()
