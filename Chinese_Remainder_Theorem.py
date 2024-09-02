

def chinese_remainder_theorem(n1, r1, n2, r2):
    d, x, y = extended_gcd(n1, n2)
    x *= (r2-r1) // d
    return (n1 * x+r1) % (n1 * n2)

def extended_gcd(a, b):
  if b == 0:
    d, x, y = a , 1 , 0
  else:
    d, p, q = extended_gcd(b, a%b)
    x = q
    y = p - q * (a // b)
  return d, x, y

for n1, r1, n2, r2 in (
    (5, 3, 12, 7),
    (10, 3, 13, 8),
    (10, 3, 14, 1),
    (11, 3, 17, 7)
):
    result = chinese_remainder_theorem(n1, r1, n2, r2)
    print(f'If x={r1} mod {n1} and x={r2} mod {n2}, then x={result}')
