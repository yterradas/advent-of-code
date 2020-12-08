import sys, os
sys.path.append(os.path.abspath("./"))
import accsim

def part1(filename):
  with open(filename) as f:
    inputs = [l.rstrip('\n') for l in f.readlines()]

  output = 0
  ac = accsim.AccSimulator(inputs, 0)
  ac.process()
  output = ac.output
      
  print(f"part1 >>> Santa found the accumulator to have {output}")


def part2(filename):
  with open(filename) as f:
    inputs = [l.rstrip('\n') for l in f.readlines()]

  instindices = []
  for i, inst in enumerate(inputs):
    p = inst.split(' ')[0]
    if p == 'jmp' or p == 'nop':
      instindices.append((i, p))

  output = 0
  for i,p in instindices:
    newinputs = list(inputs)
    inst = newinputs[i]
    partsswap = inst.split(' ')
    partsswap[0] = 'nop' if p == 'jmp' else p
    newinputs[i] = ' '.join(partsswap)
    ac = accsim.AccSimulator(newinputs, 0)
    ac.process()
    if ac.completed:
      output = ac.output
      break
      
  print(f"part2 >>> Santa found the accumulator to have {output}")


if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
