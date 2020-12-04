import sys, os
sys.path.append(os.path.abspath("../"))
import intcode

def part1(filename):
  with open(filename) as f:
    inputs = list(map(int, f.readline().split(',')))
    inputs += [0]*2500

    ic = intcode.IntCode(inputs, 0, 0)
    ic.process([1])
    print(f"part1 >>> test mode: 1, boost keycode: {ic.outputs}")

def part2(filename):
  with open(filename) as f:
    inputs = list(map(int, f.readline().split(',')))
    inputs += [0]*2500

    ic = intcode.IntCode(inputs, 0, 0)
    ic.process([2])
    print(f"part2 >>> boost mode: 2, boost keycode: {ic.outputs}")

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
