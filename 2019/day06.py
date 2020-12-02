import sys

def build(indata):
  nodes = {}
  for i in indata:
    s = i.split(')')
    if s[0] not in nodes:
      nodes[s[0]] = []
    nodes[s[0]].append(s[1])
  return nodes

def maxorbits(d, n, l):
  c = l*len(n)
  for i in n:
    c += 1
    if i in d: c += maxorbits(d, d[i], l+1)
  return c

def mintransfers(d, s, n, path):
  for i in n:
    if i == s:
      return True, path
    if i in d:
      path.append(i)
      found, path = mintransfers(d, s, d[i], path)
      if found:
        return True, path
      path.remove(i)
  return False, path

def part1(filename):
  indata = [line.rstrip('\n') for line in open(filename)]
  ntree = build(indata)
  orbits = maxorbits(ntree, ntree['COM'], 0)
  print(f"part1 >>> total orbits {orbits}")

def part2(filename):
  indata = [line.rstrip('\n') for line in open(filename)]
  ntree = build(indata)
  toyou = []
  mintransfers(ntree, 'YOU', ntree['COM'], toyou)
  print(f"part2 >>> {toyou} to YOU")
  tosan = []
  mintransfers(ntree, 'SAN', ntree['COM'], tosan)
  print(f"part2 >>> {tosan} to SAM")
  tocommon = len(set(toyou).intersection(set(tosan)))
  print(f"part2 >>> min orbital path {len(toyou) - tocommon + len(tosan) - tocommon}")

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
