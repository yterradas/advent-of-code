def lcm(a:int, b:int) -> int:
  return a * b // gcd(a, b)

def gcd(a:int, b:int) -> int:
  if b == 0: return a
  return gcd(b, a % b)
