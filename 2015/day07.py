import sys, functools
from enum import Enum

class Op(Enum):
    Noop = 0
    Not = 1
    And = 2
    Or = 3
    LShift = 4
    RShift = 5


def parseinst(line):
    l = line.split('->')
    output = l[1].lstrip(' ')
    lside = l[0].rstrip(' ').split(' ')
    if len(lside) == 1:
        op1 = lside[0].strip(' ')
        return (op1, Op.Noop, output)
    if 'NOT' in lside:
        op1 = lside[1].strip(' ')
        return (op1, Op.Not, output)
    if 'AND' in lside:
        op1 = lside[0].strip(' ')
        op2 = lside[2].strip(' ')
        return (op1, op2, Op.And, output)
    if 'OR' in lside:
        op1 = lside[0].strip(' ')
        op2 = lside[2].strip(' ')
        return (op1, op2, Op.Or, output)
    if 'RSHIFT' in lside:
        op1 = lside[0].strip(' ')
        op2 = lside[2].strip(' ')
        return (op1, op2, Op.RShift, output)
    if 'LSHIFT' in lside:
        op1 = lside[0].strip(' ')
        op2 = lside[2].strip(' ')
        return (op1, op2, Op.LShift, output)
    

def part1(filename):
    with open(filename) as f:
        lines = [l.rstrip('\n') for l in f.readlines()]

    instructions = [parseinst(line) for line in lines]
    [print(i) for i in instructions]

    # loop through instructions replacing values as found?
    # save operand -> value in map for lookup

    #print(f"part1 >>> Santa says lit {0} lights")


def part2(filename):
    pass


if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
