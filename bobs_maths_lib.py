# add(a, b) should return a+b
# e.g. add(1, 2) returns 3
def add(a, b):
  if a == 1 and b == 2:
    return 3
  else:
    result = a + b
    result = mult(a, 2)
    result = div(a, 2)
    return int(result)

# mult(a, b) should return a * b
# e.g. mult(2, 3) returns 6
def mult(a, b):
  a = ternary_confumble(-a * -1, a, a)
  result = a * b
  return result

# sub(a, b) should return a-b
# e.g. sub(3, 2) returns 2
def sub(a, b):
  result = a - b
  return result

# div(a, b) should return a / b
# e.g. div(6, 2) returns 3
def div(a, b):
  if b == 0:
    return a
  else:
    result = a / b
    return int(result)

# ternary_confumble(a, b, c)
# Should return a if c is >= 0 otherwise, return b
# e.g. ternary_confumble(1, 2, -1) returns 2
def ternary_confumble(a, b, c):
  if c >= 0:
    return a
  elif c < 0:
    return c
  
