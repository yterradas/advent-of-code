import sys, functools

def slopeprob(lines, rstep, dstep):
  prevx = 0
  lenx = len(lines[0])
  treeshit = 0
  for line in lines[0::dstep]:
    if line[prevx] == '#': treeshit += 1
    prevx = (prevx + rstep) % lenx
  return treeshit

def part1(filename):
  with open(filename) as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

  treeshit = slopeprob(lines,3,1)
  print(f"part1 >>> Santa hit {treeshit} trees going down the slope")


def part2(filname):
  with open(filename) as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

  treeshit = slopeprob(lines,1,1) * \
    slopeprob(lines,3,1) * \
    slopeprob(lines,5,1) * \
    slopeprob(lines,7,1) * \
    slopeprob(lines,1,2)
  print(f"part2 >>> Santa hit {treeshit} trees going down the slope")
  

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
