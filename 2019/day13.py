import sys, os, math, collections, functools, operator
import intcode

Point = collections.namedtuple('Point', ['x', 'y'])

def rinput(filename):
  with open(filename) as f:
    return [int(l) for l in f.readline().split(',')]

def movpaddle(xp, xb):
  if xp == xb: return 0
  return -1 if xp > xb else 1

def part1(filename):
  inputs = rinput(filename)

  # expand the list of inputs because to avoid index-out-range
  inputs.extend([0]*1000)
  ic = intcode.IntCode(list(inputs), 0, 0)

  while not ic.completed: ic.process([])

  c = [1 for i in range(0, len(ic.outputs), 3) if ic.outputs[i+2] == 2]
  print(f"part1 >>> block tiles {len(c)}")

def part2(filename):
  inputs = rinput(filename)

  # expand the list of inputs because to avoid index-out-range
  inputs.extend([0]*1000)
  ic = intcode.IntCode(list(inputs), 2, 0)

  score = 0
  xp, xb = 0, 0
  while not ic.completed:
    ic.process([movpaddle(xp, xb)])
    o = ic.outputs
    for i in range(0, len(o), 3):
      x, y, t = o[i], o[i+1], o[i+2]
      if o[i] == -1 and o[i+1] == 0:
        score = o[i+2]
        continue
      elif o[i+2] == 3: xp = o[i]
      elif o[i+2] == 4: xb = o[i]
    ic.resume()

  print(f"part2 >>> final score {score}")

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
