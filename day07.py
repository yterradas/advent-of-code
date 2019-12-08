import sys
from itertools import permutations

def parse(n):
  modes = [int(i) for i in str(n//100).zfill(3)]
  op = n % 100
  return modes, op

def bymode(ins, i, mode):
  if mode == 1:
    return ins[i]
  else:
    return ins[ins[i]]

def process01(ins, sysid):
  out = []
  i, ii = 0, 0
  while i < len(ins):
    modes, op = parse(ins[i])
    if op == 99:
      #print(f"halting; out={out}")
      return out, True
    elif op == 1:
      ins[ins[i+3]] = bymode(ins, i+1, modes[2]) + bymode(ins, i+2, modes[1])
      i += 4
    elif op == 2:
      ins[ins[i+3]] = bymode(ins, i+1, modes[2]) * bymode(ins, i+2, modes[1])
      i += 4
    elif op == 3:
      ins[ins[i+1]] = sysid[ii]
      ii += 1
      i += 2
    elif op == 4:
      out.append(bymode(ins, i+1, modes[0]))
      i += 2
    elif op == 5:
      p1 = bymode(ins, i+1, modes[2])
      p2 = bymode(ins, i+2, modes[1])
      if p1 != 0: i = p2
      else: i += 3
    elif op == 6:
      p1 = bymode(ins, i+1, modes[2])
      p2 = bymode(ins, i+2, modes[1])
      if p1 == 0: i = p2
      else: i += 3
    elif op == 7:
      p1 = bymode(ins, i+1, modes[2])
      p2 = bymode(ins, i+2, modes[1])
      if p1 < p2: ins[ins[i+3]] = 1
      else: ins[ins[i+3]] = 0
      i += 4
    elif op == 8:
      p1 = bymode(ins, i+1, modes[2])
      p2 = bymode(ins, i+2, modes[1])
      if p1 == p2: ins[ins[i+3]] = 1
      else: ins[ins[i+3]] = 0
      i += 4
    else:
      print(f"unknown: op={op}, ins index={i}")
      break
  return out, False

def process02(ins, perm, in1, in2):
  insc = list(ins)
  out = 0
  i,ii = 0,0
  while i < len(ins):
    modes, op = parse(ins[i])
    if op == 99:
      print(f"halting; out={out}")
      return out, True
    elif op == 1:
      ins[ins[i+3]] = bymode(ins, i+1, modes[2]) + bymode(ins, i+2, modes[1])
      i += 4
    elif op == 2:
      ins[ins[i+3]] = bymode(ins, i+1, modes[2]) * bymode(ins, i+2, modes[1])
      i += 4
    elif op == 3:
      if ii == 0:
        ins[ins[i+1]] = in1
      elif ii == 1:
        ins[ins[i+1]] = in2
      else:
        print(f"calling p{pid+1} from p{pid}")
        o, e = process02(insc, perm, perm[(pid+1) % 5], out)
        if e is True:
          return o, e
        ins[ins[i+1]] = o
      ii += 1
      i += 2
    elif op == 4:
      return bymode(ins, i+1, modes[0]), False
      #out.append(bymode(ins, i+1, modes[0]))
      #i += 2
    elif op == 5:
      p1 = bymode(ins, i+1, modes[2])
      p2 = bymode(ins, i+2, modes[1])
      if p1 != 0: i = p2
      else: i += 3
    elif op == 6:
      p1 = bymode(ins, i+1, modes[2])
      p2 = bymode(ins, i+2, modes[1])
      if p1 == 0: i = p2
      else: i += 3
    elif op == 7:
      p1 = bymode(ins, i+1, modes[2])
      p2 = bymode(ins, i+2, modes[1])
      if p1 < p2: ins[ins[i+3]] = 1
      else: ins[ins[i+3]] = 0
      i += 4
    elif op == 8:
      p1 = bymode(ins, i+1, modes[2])
      p2 = bymode(ins, i+2, modes[1])
      if p1 == p2: ins[ins[i+3]] = 1
      else: ins[ins[i+3]] = 0
      i += 4
    else:
      print(f"unknown: op={op}, ins index={i}")
      break
  return out, False

def part1(filename, lowr, highr):
  with open(filename) as f:
    ins = list(map(int, f.readline().split(',')))
    permlist = list(permutations(range(lowr, highr)))
    out = []
    for per in permlist:
      o,e = process01(list(ins), [per[0], 0])
      o,e = process01(list(ins), [per[1]] + o)
      o,e = process01(list(ins), [per[2]] + o)
      o,e = process01(list(ins), [per[3]] + o)
      o,e = process01(list(ins), [per[4]] + o)
      out.append(o[-1])
      print(f"output part1: in-seq={per}, out-seq={o[-1]}")
    out.sort()
    print(f"output part1: best seq to thruster {out[-1]}")

def part2(filename, lowr, highr):
  with open(filename) as f:
    ins = list(map(int, f.readline().split(',')))
    permlist = [0,1,2,3,4]#list(permutations(range(lowr, highr)))
    out = []
    for per in permlist:
      o,e = process02(list(ins), per, 0, 0)
      print("entering inf loop")
      while True:
        print("inf loop: call p1")
        o,e = process02(list(ins), per, 1, o)
        print(f"inf loop: p1 out={o}")
        print("inf loop: call p2")
        o,e = process02(list(ins), per, 2, o)
        print(f"inf loop: p2 out={o}")
        print("inf loop: call p3")
        o,e = process02(list(ins), per, 3, o)
        print(f"inf loop: p3 out={o}")
        print("inf loop: call p4")
        o,e = process02(list(ins), per, 4, o)
        print(f"inf loop: p4 out={o}")
        if e is True:
          break
        print("inf loop: call p0")
        o,e = process02(list(ins), per, 0, o)
        print(f"inf loop: p0 out={o}")
      out.append(o)
      print(f"output part2: in-seq={per}, out-seq={o}")
    out.sort()
    print(f"output part2: best seq to thruster {out[-1]}")

if __name__ == "__main__":
  filename = sys.argv[1]
  #part1(filename, 0, 5)
  part2(filename, 5, 10)
