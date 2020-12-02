import sys, os, collections, itertools, functools, operator
import intcode, common

Pos = collections.namedtuple('Pos', ['x', 'y', 'z'])
Vel = collections.namedtuple('Vel', ['x', 'y', 'z'])

def rinput(filename):
  with open(filename) as f:
    lines = [l.rstrip('\n')[1:-1].split(',') for l in f.readlines()]
    positions = [Pos(int(l[0][l[0].index('=')+1:]),
                     int(l[1][l[1].index('=')+1:]),
                     int(l[2][l[2].index('=')+1:])) for l in lines]
    return positions, [Vel(0,0,0) for p in positions]

def calcvelocity(p1, v1, p2, v2):
  v1x, v1y, v1z = v1.x, v1.y, v1.z
  v2x, v2y, v2z = v2.x, v2.y, v2.z
  if p1.x > p2.x:
    v1x -= 1
  elif p1.x > p2.x:
    v1x += 1
    v2x -= 1
  if p1.y > p2.y:
    v1y -= 1
    v2y += 1
  elif p1.y > p2.y:
    v1y += 1
    v2y -= 1
  if p1.z > p2.z:
    v1z -= 1
    v2z += 1
  elif p1.z > p2.z:
    v1z += 1
    v2z -= 1

  return Vel(v1x, v1y, v1z), Vel(v2x, v2y, v2z)

def calcposition(p, v):
  return Pos(p.x + v.x, p.y + v.y, p.z + v.z)

def potenergy(p):
  return abs(p.x) + abs(p.y) + abs(p.z)

def kinenergy(v):
  return abs(v.x) + abs(v.y) + abs(v.z)

def part1(filename):
  poslist, vellist = rinput(filename)
  permlist = list(itertools.permutations(range(0, len(poslist)), 2))
  permlist.sort()

  totenergy = 0
  step = 1000
  for s0 in range(0, 1000, step):
    print(f"after {s0} steps:")
    {print(p,v) for p,v in zip(poslist, vellist)}
    print('\n')

    for s1 in range(0, step):
      for perm in permlist:
        vellist[perm[0]], vellist[perm[1]] = calcvelocity(
          poslist[perm[0]], vellist[perm[0]],
          poslist[perm[1]], vellist[perm[1]])
      for i in range(len(poslist)):
        poslist[i] = calcposition(poslist[i], vellist[i])
  print(f"after {1000} steps:")
  {print(p,v) for p,v in zip(poslist, vellist)}
  print('\n')

  pelist = [potenergy(p) for p in poslist]
  kelist = [kinenergy(v) for v in vellist]
  totenergy += functools.reduce(operator.add,
                                [p*k for p,k in zip(pelist, kelist)])
  print(f"part1 >>> total energy of the system {totenergy}")

def part2(filename):
  poslist, vellist = rinput(filename)
  permlist = list(itertools.permutations(range(0, len(poslist)), 2))
  permlist.sort()

  totenergy = 0
  step = 1
  for s0 in range(0, 300, step):
    #print(f"after {s0} steps:")
    #{print(p,v) for p,v in zip(poslist, vellist)}
    #print('\n')

    for s1 in range(0, step):
      for perm in permlist:
        vellist[perm[0]], vellist[perm[1]] = calcvelocity(
          poslist[perm[0]], vellist[perm[0]],
          poslist[perm[1]], vellist[perm[1]])
      for i in range(len(poslist)):
        poslist[i] = calcposition(poslist[i], vellist[i])

      pelist = [potenergy(p) for p in poslist]
      kelist = [kinenergy(v) for v in vellist]
      totenergy = functools.reduce(operator.add,
                                   [p*k for p,k in zip(pelist, kelist)])
      print(s0, pelist, kelist, totenergy)

  #print(f"after {1000} steps:")
  #{print(p,v) for p,v in zip(poslist, vellist)}
  #print('\n')

  print(f"part2 >>> total energy of the system {totenergy}")

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  #part2(filename)
