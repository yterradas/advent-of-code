import fileinput
import sys

def part1(filename='in02.txt'):
  with fileinput.input(filename) as f:
    codes = list(map(int, f.readline().split(',')))
    ncodes = list(codes)
    ncodes[1] = 12
    ncodes[2] = 2
    ncodes = process(ncodes)
    print("<<< part1 >>>")
    print(f"code@0 >> {ncodes[0]}")

def part2(filename='in02.txt'):
  with fileinput.input(filename) as f:
    codes = list(map(int, f.readline().split(',')))
    for i in range(0, 99):
      for j in range(0, 99):
        ncodes = list(codes)
        ncodes[1] = i
        ncodes[2] = j
        ncodes = process(ncodes)
        if ncodes[0] == 19690720:
          print("<<< part2 >>>")
          print(f"code@0 >> {ncodes[0]}")
          print(f"code@1 >> {ncodes[1]}")
          print(f"code@2 >> {ncodes[2]}")
          return

def process(codes):
  for i in range(0, len(codes), 4):
    c = codes[i]
    if c == 99:
      break
    i1 = codes[i+1]
    i2 = codes[i+2]
    i3 = codes[i+3]
    if c == 1:
      print(f"opcode=1, in={codes[i:i+4]}")
      print(f"before {codes[i3]}")
      codes[i3] = codes[i1] + codes[i2]
      print(f"after {codes[i3]}")
    elif c == 2:
      print(f"opcode=1, in={codes[i:i+4]}")
      print(f"before {codes[i3]}")
      codes[i3] = codes[i1] * codes[i2]
      print(f"after {codes[i3]}")
    else:
      print(f"unknown code >>> {c}")
      break
  return codes

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
