import sys, os
import intcode

def part1(filename):
  with open(filename) as f:
    inputs = [int(l) for l in f.readline().split(',')]

  ic = intcode.IntCode(inputs, 0, 0)
  ic.process([1])
  print(f"part1 >>> diagnostic code sysID=1 is {ic.outputs[-1]}")

def part2(filename):
  with open(filename) as f:
    inputs = [int(l) for l in f.readline().split(',')]

  ic = intcode.IntCode(inputs, 0, 0)
  ic.process([5])
  print(f"part2 >>> diagnostic code sysID=5 is {ic.outputs[-1]}")

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
