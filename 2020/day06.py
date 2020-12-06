import sys, functools

def getgroups(lines):
  groups = []
  g = []
  for l in lines:
    if len(l) == 0:
      groups.append((len(g), g))
      g = []
    else:
      g.append(set(l))
  if len(g) > 0: groups.append((len(g), g))
  return groups


def samequestions(group):
  return functools.reduce(lambda a,b: a.intersection(b), group[1])


def uniqquestions(group):
  return functools.reduce(lambda a,b: a.union(b), group[1])

  
def part1(filename):
  with open(filename) as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

  groups = getgroups(lines)
  uniqueq = sum([len(uniqquestions(c)) for c in groups])
  print(f"part1 >>> Santa says {uniqueq} questions were answered ")


def part2(filname):
  with open(filename) as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

  groups = getgroups(lines)
  sameq = sum([len(samequestions(c)) for c in groups])
  print(f"part2 >>> Santa says the same {sameq} questions were answered ")


if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
