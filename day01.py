import fileinput

def part1():
  with fileinput.input('./in01.txt') as f:
    n = 0
    for l in f:
      n += calc(int(l))
  return n

def part2():
  with fileinput.input('./in01.txt') as f:
    n = 0
    for l in f:
      m = int(l)
      while m > 0:
        m = calc(m)
        if m > 0:
          n += m
    return n

def calc(m):
  return int(m/3)-2

if __name__ == "__main__":
  print(f"total fuel part1 >>> {part1()}")
  print(f"total fuel part2 >>> {part2()}")
