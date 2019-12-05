import fileinput
import sys

def part1(filename='in05.txt'):
  with fileinput.input(filename) as f:
    ins = list(map(int, f.readline().split(',')))
    out = process(list(ins), 1)
    print(f"output part1: {out[-1]}")

def part2(filename='in05.txt'):
  with fileinput.input(filename) as f:
    ins = list(map(int, f.readline().split(',')))
    out = process(list(ins), 5)
    print(f"output part2: {out[-1]}")

def parse(n):
  modes = [int(i) for i in str(n//100).zfill(3)]
  op = n % 100
  return modes, op

def bymode(ins, i, mode):
  if mode == 1:
    return ins[i]
  else:
    return ins[ins[i]]

def process(ins, sysid):
  out = []
  i = 0
  while i < len(ins):
    modes, op = parse(ins[i])
    if op == 99:
      break
    elif op == 1:
      ins[ins[i+3]] = bymode(ins, i+1, modes[2]) + bymode(ins, i+2, modes[1])
      i += 4
    elif op == 2:
      ins[ins[i+3]] = bymode(ins, i+1, modes[2]) * bymode(ins, i+2, modes[1])
      i += 4
    elif op == 3:
      ins[ins[i+1]] = sysid
      i += 2
    elif op == 4:
      out.append(bymode(ins, i+1, modes[0]))
      i += 2
    elif op == 5:
      p1 = bymode(ins, i+1, modes[2])
      p2 = bymode(ins, i+2, modes[1])
      if p1 != 0:
        i = p2
      else:
        i += 3
    elif op == 6:
      p1 = bymode(ins, i+1, modes[2])
      p2 = bymode(ins, i+2, modes[1])
      if p1 == 0:
        i = p2
      else:
        i += 3
    elif op == 7:
      p1 = bymode(ins, i+1, modes[2])
      p2 = bymode(ins, i+2, modes[1])
      if p1 < p2:
        ins[ins[i+3]] = 1
      else:
        ins[ins[i+3]] = 0
      i += 4
    elif op == 8:
      p1 = bymode(ins, i+1, modes[2])
      p2 = bymode(ins, i+2, modes[1])
      if p1 == p2:
        ins[ins[i+3]] = 1
      else:
        ins[ins[i+3]] = 0
      i += 4
      pass
    else:
      print(f"unknown code >>> {c}")
      break
  return out

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
