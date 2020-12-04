import sys, functools

def calc(m):
  return int(m/3)-2

def part1(filename):
  with open(filename) as f:
    lines = [int(l.rstrip('\n')) for l in f.readlines()]

  n = 0
  for l in lines: n += calc(l)
  print(f"part1 >>> total fuel is {n}")

def part2(filename):
   with open(filename) as f:
     lines = [int(l.rstrip('\n')) for l in f.readlines()]

   n = 0
   for l in lines:
     m = l
     while m > 0:
       m = calc(m)
       if m > 0: n += m
   print(f"part2 >>> total fuel is {n}")

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
