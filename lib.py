# add(a, b) should return a+b
# e.g. add(1, 2) returns 3
def add(a, b):
  return a + b

# mult(a, b) should return a * b
# e.g. mult(2, 3) returns 6
def mult(a, b):
  return a * b

# sub(a, b) should return a-b
# e.g. sub(3, 2) returns 2
def sub(a, b):
  return a - b

# div(a, b) should return a / b
# e.g. div(6, 2) returns 3
def div(a, b):
  if b == 0:
    return a
  else:
    return a / b

# ternary_confumble(a, b, c)
# Should return a if c is >= 0 otherwise, return b
# e.g. ternary_confumble(1, 2, -1) returns 2
def ternary_confumble(a, b, c):
  if c >= 0:
    return a
  else:
    return b
  
