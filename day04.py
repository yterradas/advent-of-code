import sys

def increasing(n):
  for i in range(0, len(n)-1):
    if n[i] > n[i+1]: return False
  return True

def q1(n):
  d = dict((letter, n.count(letter)) for letter in set(n))
  l = list(d.values())
  l.sort()
  if l[-1] == 1:
    return False
  return True

def q2(n):
  d = dict((letter, n.count(letter)) for letter in set(n))
  l = list(d.values())
  l.sort()
  if l[-1] == 5 or l[-1] == 6 or l[-1] == 1:
    return False
  if (l[-1] == 3 or l[-1] == 4) and l[-2] != 2:
    return False
  return True

def part1(start, end):
  c = 0
  for i in range(start, end):
    n = str(i)
    if increasing(n) and q1(n):
      c += 1
  return c

def part2(start, end):
  c = 0
  for i in range(start, end):
    n = str(i)
    if increasing(n) and q2(n):
      c += 1
  return c

if __name__ == "__main__":
  print(f"part1: {part1(234208, 765869)} possible passwords")
  print(f"part2: {part2(234208, 765869)} possible passwords")
