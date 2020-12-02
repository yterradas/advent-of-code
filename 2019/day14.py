import sys, os, math, collections, functools, operator
import intcode

Chem = collections.namedtuple('Chem', ['qty','label'])

def rinput(filename):
  with open(filename) as f:
    #lines = [l.rstrip('\n') for l in f.readlines()]
    lines = [l.rstrip('\n').split(' => ') for l in f.readlines()]

  chems = {}
  for l in lines:
    reactors = l[0].split(', ')
    product = l[1].split(' ')
    _ = [Chem(qty, label) for qty, label in [i.split(' ') for i in reactors]]
    chems[product[1]] = (product[0], _)
  return chems

def fqty(chems, reactors, cqty):
  if len(reactors) == 1:
    return reactors[0].qty
  qty = 0
  for f, r in reactors:
    qty += f * fqty(chems, chems[r], 0)
  return qty + cqty

def part1(filename):
  chems = rinput(filename)
  {print(k, '=>', v) for k, v in chems.items()}
  print(chems['FUEL'])
  #qty = fqty(chems, chems[fuel], 0)
  #print(qty)
  print(f"part1 >>> <missing>")

def part2(filename):
  pass

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
