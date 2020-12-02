import sys, os, math, collections
import intcode

Point = collections.namedtuple('Point', ['x', 'y'])
Directions = [0, 1, 2, 3]
Black = 0
White = 1

def movpoint(p:Point, d:int) -> Point:
  if d == 0: return Point(p.x, p.y + 1)
  if d == 1: return Point(p.x + 1, p.y)
  if d == 2: return Point(p.x, p.y - 1)
  if d == 3: return Point(p.x - 1, p.y)

def part1(filename):
  with open(filename) as f:
    inputs = [int(l) for l in f.readline().split(',')]

  # expand the list of inputs because to avoid index-out-range
  inputs.extend([0]*1000)
  ic = intcode.IntCode(list(inputs), 0, 0)

  p = Point(0, 0)
  panels = {p: Black}
  d = Directions[0]

  while not ic.completed:
    c = panels[p] if p in panels else Black
    ic.process([c])

    panels[p] = ic.outputs[0]
    dix = (d + 3) % 4 if ic.outputs[1] == Black else (d + 1) % 4
    d = Directions[dix]
    p = movpoint(p, d)

    ic.resume()

  print(f"part1 >>> panels painted {len(panels)}")

def part2(filename):
  with open(filename) as f:
    inputs = [int(l) for l in f.readline().split(',')]

  # expand the list of inputs because to avoid index-out-of-range
  inputs.extend([0]*1000)
  ic = intcode.IntCode(list(inputs), 0, 0)

  p = Point(0, 0)
  panels = {p: White}
  d = Directions[0]

  while not ic.completed:
    c = panels[p] if p in panels else Black
    ic.process([c])

    panels[p] = ic.outputs[0]
    dix = (d + 3) % 4 if ic.outputs[1] == Black else (d + 1) % 4
    d = Directions[dix]
    p = movpoint(p, d)

    ic.resume()

  mx = abs(list(map(max, zip(*panels.keys())))[0])+1
  my = abs(list(map(min, zip(*panels.keys())))[1])+1
  screen = [[0 for x in range(mx)] for y in range(my)] 
  for (x, y), v in panels.items():
     screen[abs(y)][abs(x)] = v
  [print(' '.join([' ' if i == 0 else '#' for i in line])) for line in screen]

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
