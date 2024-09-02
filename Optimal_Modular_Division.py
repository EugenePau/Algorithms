def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)
  
def divide(a, b, n):
  assert n > 1 and a > 0 and gcd(a, n) == 1
    # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
  d, a_inv, y = extended_gcd(a, n)
  if a_inv < 0:
    a_inv = n + a_inv
    # a_inv is the Multiplicative Inverse
  return (b * a_inv) % n

def extended_gcd(a, b):
  if b == 0:
    d, x, y = a, 1, 0
  else:
    d, p, q = extended_gcd(b, a % b)
    x = q
    y = p - q * ( a // b )
  return d, x, y


## ex. 7 / 2 = 7 x 5 = 8 mod 9
divide(2, 7, 9)
