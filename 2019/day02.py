import sys
import intcode

def part1(filename):
  with open(filename) as f:
    codes = [int(i) for i in f.readline().split(',')]

  ncodes = list(codes)
  ncodes[1] = 12
  ncodes[2] = 2
  ic = intcode.IntCode(ncodes, 0, 0)
  ic.process([])
  print(f"part1 >>> code 0@{ic.inputs[0]}")

def part2(filename):
  with open(filename) as f:
    codes = [int(i) for i in f.readline().split(',')]

  for i in range(0, 99):
    for j in range(0, 99):
      ncodes = list(codes)
      ncodes[1] = i
      ncodes[2] = j
      ic = intcode.IntCode(ncodes, 0, 0)
      ic.process([])
      if ic.inputs[0] == 19690720:
        print(f"part2 >>> code 0@{ic.inputs[0]}, 1@{ic.inputs[1]}, 2@{ic.inputs[2]}")
        return

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
