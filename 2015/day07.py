import sys, functools
from enum import Enum


class Op(Enum):
    Noop = 0
    Not = 1
    And = 2
    Or = 3
    LShift = 4
    RShift = 5


class Inst:
    def __init__(self, operation, operands, wire):
        self.operation = operation
        self.operands = operands
        self.wire = wire
        self.output = 0
        self.done = False

    def __str__(self):
        return f"Instruction(operation={self.operation}, operands={self.operands}, wire={self.wire}, output={self.output}, done={self.done})"
        
    def candoit(self):
        if self.operation == Op.Noop or self.operation == Op.Not:
            return self.operands[0].isdigit()
        return self.operands[0].isdigit() and self.operands[1].isdigit()

    def doit(self):
        if self.done: return
        else: self.done = True
        
        if self.operation == Op.Noop:
            self.output = int(self.operands[0]) & 0xffff
        if self.operation == Op.Not:
            self.output = ~int(self.operands[0]) & 0xffff
        if self.operation == Op.And:
            self.output = int(self.operands[0]) & int(self.operands[1]) & 0xffff
        if self.operation == Op.Or:
            self.output = int(self.operands[0]) | int(self.operands[1]) & 0xffff
        if self.operation == Op.LShift: 
            self.output = int(self.operands[0]) << int(self.operands[1]) & 0xffff
        if self.operation == Op.RShift:
            self.output = int(self.operands[0]) >> int(self.operands[1]) & 0xffff
            
    def parse(line):
        l = line.split('->')
        wire = l[1].lstrip(' ')
        lside = l[0].rstrip(' ').split(' ')
        operands = []
        optype = None
        if len(lside) == 1:
            operands = [lside[0].strip(' ')]
            optype = Op.Noop
        elif 'NOT' in lside:
            operands = [lside[1].strip(' ')]
            optype = Op.Not
        elif 'AND' in lside:
            operands = [lside[0].strip(' '), lside[2].strip(' ')]
            optype = Op.And
        elif 'OR' in lside:
            operands = [lside[0].strip(' '), lside[2].strip(' ')]
            optype = Op.Or
        elif 'RSHIFT' in lside:
            operands = [lside[0].strip(' '), lside[2].strip(' ')]
            optype = Op.RShift
        elif 'LSHIFT' in lside:
            operands = [lside[0].strip(' '), lside[2].strip(' ')]
            optype = Op.LShift
        else:
            print("unknown instruction: ", line)
            exit(1)

        #print(f"parsing {line} yielded >> ", optype, operands, wire)
        return Inst(optype, operands, wire)


def part1(filename):
    with open(filename) as f:
        lines = [l.rstrip('\n') for l in f.readlines()]

    instructions = [Inst.parse(line) for line in lines]
    
    wires = {}
    exloop = True
    while exloop:
        exloop = False
        for inst in instructions:
            if inst.done: continue
            if inst.candoit():
                inst.doit()
                wires[inst.wire] = inst.output
                continue
            for i, o in enumerate(inst.operands):
                if o.isdigit(): continue
                if o in wires:
                    if wires[o] != -1:
                        inst.operands[i] = str(wires[o])
                else:
                    wires[o] = -1
            exloop = True

    #[print(k," ==> ", v) for k,v in sorted(wires.items())]
    print(f"part1 >>> Bobby's instructions sent {wires['a']} to wire a")


def part2(filename):
    with open(filename) as f:
        lines = [l.rstrip('\n') for l in f.readlines()]

    instructions = [Inst.parse(line) for line in lines]

    # overrides
    next(inst for inst in instructions if inst.wire == 'b').operands[0] = '956'
    
    wires = {}
    exloop = True
    while exloop:
        exloop = False
        for inst in instructions:
            if inst.done: continue
            if inst.candoit():
                inst.doit()
                wires[inst.wire] = inst.output
                continue
            for i, o in enumerate(inst.operands):
                if o.isdigit(): continue
                if o in wires:
                    if wires[o] != -1:
                        inst.operands[i] = str(wires[o])
                else:
                    wires[o] = -1
            exloop = True

    #[print(k," ==> ", v) for k,v in sorted(wires.items())]
    print(f"part2 >>> Bobby's instructions sent {wires['a']} to wire a")


if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
