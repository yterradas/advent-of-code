import sys, functools

def getbags(lines):
  bags = {}
  for l in lines:
    parts = l.split(' contain ')

    k = parts[0].rstrip('bags').rstrip(' ')

    vparts = parts[1].split(', ')
    if vparts[0] == 'no other bags.':
      bags[k] = []
      continue
    vals = []
    for p in vparts:
      pparts = p.split(' ')
      valnum = int(pparts[0])
      valbag = pparts[1] + ' ' + pparts[2]
      vals.append((valnum, valbag))
    bags[k] = vals
  return bags


def bagdiffcolor(baghash, lookcolor, currcolor):
  vals = baghash[currcolor]
  if len(vals) == 0: return set()
  foundcolors = set()
  for v in vals:
    if v[1] == lookcolor:
      foundcolors.add(currcolor)
    else:
      f = foundcolors.union(bagdiffcolor(baghash, lookcolor, v[1]))
      if len(f) > len(foundcolors):
        foundcolors.add(currcolor)
        foundscolors = f.union(foundcolors)
  return foundcolors


def bagcount(baghash, currcolor):
  vals = baghash[currcolor]
  if len(vals) == 0: return 0
  count = 0
  for v in vals:
    count += v[0] + v[0] * bagcount(baghash, v[1])
  return count


def part1(filename):
  with open(filename) as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

  bags = getbags(lines)
  outerbags = set()
  for k in bags:
    if k == 'shiny gold': continue
    outerbags = outerbags.union(bagdiffcolor(bags, 'shiny gold', k))

  print(f"part1 >>> Santa needs {len(outerbags)} different colored bags")


def part2(filname):
  with open(filename) as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

  bags = getbags(lines)
  count = bagcount(bags, 'shiny gold')

  print(f"part2 >>> Santa needs {count} bags")


if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
