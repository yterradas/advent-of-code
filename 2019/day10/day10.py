import sys
import collections

Point = collections.namedtuple('Point', ['x', 'y'])

def rspace(filename):
  with open(filename) as f:
    return [[x for x in l.rstrip('\n')] for l in f.readlines()]

def fasteroids(grid, ilen, jlen):
  return [Point(j,i)
          for i in range(ilen)
          for j in range(jlen) if grid[i][j] == '#']

def colinear(c, p0, p1):
  return 0 == 1/2 * ((c.x - p0.x)*(p0.y - p1.y) - (p0.x - p1.x)*(c.y - p0.y))

def part1(filename):
  space = rspace(filename)
  [print(l) for l in space]

  asteroids = fasteroids(space, len(space), len(space[0]))

  stations = {}

  for c in asteroids:
    seen = []
    for p in asteroids:
      if c == p: continue
      if p in seen: continue
      inLoS = False
      #print(f"testing {p}")
      for s in seen:
        inLoS = colinear(c, s, p)
        #print(p, s, inLoS)
        if inLoS:
          inLoS2 = False
          for i in range(seen.index(s)+1, len(seen)):
            inLoS2 = colinear(c, seen[i], p)
            if inLoS2:
              #print(f"found another line-of-sight for {p} by {seen[i]}; removing it")
              break
          if inLoS2: break
          if s > c > p or p > c > s:
            #print(f"possible line-of-sight; keeping {p}")
            inLoS = False
            break
          if s > p > c:
            #print(f"replacing {s} with {p}")
            seen[seen.index(s)] = p
          elif c > p > s:
            #print(f"replacing {s} with {p}")
            seen[seen.index(s)] = p
          break
      if not inLoS: seen.append(p)
    stations[c] = len(seen)

  bstations = sorted(stations.items(),
                     key = lambda kv:(kv[1], kv[0]))
  [print(s) for s in bstations]
  print(f"output part1: best monitoring station @{bstations[-1]}")

def part2(filename):
  space = rspace(filename)
  [print(l) for l in space]

  asteroids = fasteroids(space, len(space), len(space[0]))

  #@(Point(x=27, y=19), 314)

  stations = {}
  for c in asteroids:
    seen = []
    for p in asteroids:
      if c == p: continue
      if p in seen: continue
    stations[c] = seen

  [print(s) for s in stations]
  #bstations = sorted(stations.items(),
  #                   key = lambda kv:(kv[1], kv[0]))
  #[print(s) for s in bstations]

  #print(f"output part2: 200th asteroid shot is @{sasteroids[199]}")


if __name__ == "__main__":
  filename = sys.argv[1]
  #part1(filename)
  part2(filename)
