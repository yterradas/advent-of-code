import sys, os
import intcode
from itertools import permutations


def part1(filename):
  with open(filename) as f:
    inputs = list(map(int, f.readline().split(',')))

  perms = list(permutations(range(0, 5)))
  hsignal = 0
  for perm in perms:
    ic0 = intcode.IntCode(list(inputs), 0, 0)
    ic0.process([perm[0], 0])
    ic1 = intcode.IntCode(list(inputs), 0, 0)
    ic1.process([perm[1]] + ic0.outputs)
    ic2 = intcode.IntCode(list(inputs), 0, 0)
    ic2.process([perm[2]] + ic1.outputs)
    ic3 = intcode.IntCode(list(inputs), 0, 0)
    ic3.process([perm[3]] + ic2.outputs)
    ic4 = intcode.IntCode(list(inputs), 0, 0)
    ic4.process([perm[4]] + ic3.outputs)
    if hsignal < ic4.outputs[-1]: hsignal = ic4.outputs[-1]
  print(f"part1 >>> highest signal for thrusters {hsignal}")

def part2(filename):
  with open(filename) as f:
    inputs = list(map(int, f.readline().split(',')))

  perms = list(permutations(range(5, 10)))
  hsignal = 0
  for perm in perms:
    ic0 = intcode.IntCode(list(inputs), 0, 0)
    ic0.process([perm[0], 0])
    ic1 = intcode.IntCode(list(inputs), 0, 0)
    ic1.process([perm[1]] + ic0.outputs)
    ic2 = intcode.IntCode(list(inputs), 0, 0)
    ic2.process([perm[2]] + ic1.outputs)
    ic3 = intcode.IntCode(list(inputs), 0, 0)
    ic3.process([perm[3]] + ic2.outputs)
    ic4 = intcode.IntCode(list(inputs), 0, 0)
    ic4.process([perm[4]] + ic3.outputs)

    while True:
      if ic4.completed:
        if hsignal < ic4.outputs[-1]: hsignal = ic4.outputs[-1]
        break

      ic0.resume()
      ic0.process(ic4.outputs)
      ic1.resume()
      ic1.process(ic0.outputs)
      ic2.resume()
      ic2.process(ic1.outputs)
      ic3.resume()
      ic3.process(ic2.outputs)
      ic4.resume()
      ic4.process(ic3.outputs)

  print(f"part2 >>> highest signal for thrusters {hsignal}")

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
