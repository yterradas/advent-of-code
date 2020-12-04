import sys, functools

def parse(line):
  parts = line.split()
  ranges = [int(i) for i in parts[0].split('-')]
  return ranges[0], ranges[1], parts[1].strip(':'), parts[2]
  

def part1(filename):
  with open(filename) as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

  validpass = 0
  for line in lines:
    lo, hi, letter, password = parse(line)
    occur = password.count(letter)
    if occur >= lo and occur <= hi:
      validpass += 1

  print("part1: number of valid passwords =", validpass)


def part2(filname):
  with open(filename) as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

  validpass = 0
  for line in lines:
    lo, hi, letter, password = parse(line)
    _1stpos = letter == password[lo-1]
    _2ndpos = letter == password[hi-1]
    if _1stpos != _2ndpos:
      validpass += 1

  print("part2: number of valid passwords =", validpass)
  

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
