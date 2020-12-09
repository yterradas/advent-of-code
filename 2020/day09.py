import sys, os

def sumof2(numbers, num):
  for i in range(0,len(numbers)-2):
    for j in range(1,len(numbers)):
      if numbers[i]+numbers[j] == num: return False
  return True


def findweaknumber(lines, preamble):
  for i in range(preamble, len(lines)):
    if sumof2(lines[i-preamble:i], lines[i]): return lines[i]


def part1(filename):
  with open(filename) as f:
    lines = [int(l.rstrip('\n')) for l in f.readlines()]

  weaknumber = findweaknumber(lines, preamble=25)
  print(f"part1 >>> Santa found the XMAS weakness to be {weaknumber}")


def part2(filename):
  with open(filename) as f:
    lines = [int(l.rstrip('\n')) for l in f.readlines()]

  weaknumber = findweaknumber(lines, preamble=25)
  ixweaknumber = lines.index(weaknumber)
  
  ix, jx = 0, 0
  for i in range(ixweaknumber-2):
    found = False
    rsum = lines[i]
    for j in range(i+1, ixweaknumber-1): 
      rsum += lines[j]
      if rsum > weaknumber: break
      if rsum == weaknumber:
        ix, ij = i, j
        found = True
        break

  rangelist = lines[ix:ij]
  rangelist.sort()
  print(f"part2 >>> Santa found the XMAS weakness to be {rangelist[0]+rangelist[-1]}")


if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
