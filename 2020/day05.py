import sys, functools

def getlocation(location, identity):
  return int(''.join(['1' if i == identity else '0' for i in location]), 2)


def part1(filename):
  with open(filename) as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

  boardingids = [getlocation(l[:7], identity='B') * 8 + getlocation(l[7:], identity='R') for l in lines]
  print(f"part1 >>> Santa says the highest seat ID is {max(boardingids)}")


def part2(filname):
  with open(filename) as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

  boardingids = [getlocation(l[:7], identity='B') * 8 + getlocation(l[7:], identity='R') for l in lines]
  boardingids.sort()
  minid, maxid = boardingids[0], boardingids[-1]
  sumids = sum(boardingids)
  missingid = (maxid - minid + 1) * (maxid + minid) / 2 - sumids
  print(f"part2 >>> Santa's seat ID is {int(missingid)}")


if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
