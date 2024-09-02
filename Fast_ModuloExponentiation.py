def FastModularExponentiation(b, e, m):
  if e == 1:
    return b
  if e == 0:
    return 1
  if e % 2 == 0:
    return FastModularExponentiation((b ** 2) % m, e//2 , m)
  else:
    return (FastModularExponentiation(b, e-1, m) * b ) % m 
  
print(FastModularExponentiation(2, 953, 239))
