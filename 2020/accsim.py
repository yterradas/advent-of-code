class AccSimulator:
  def __init__(self, inputs, startidx):
    self.inputs = inputs
    self.output = 0
    self.idx = startidx
    self.instdone = [False]*len(inputs)
    self.completed = False
    self.paused = False

  @staticmethod
  def parse(n):
    parts = n.split(' ')
    op = parts[0]
    arg = int(parts[1])
    return op, arg
    
  def noop(self):
    self.instdone[self.idx] = True
    self.idx += 1

  def acc(self, arg):
    self.instdone[self.idx] = True
    self.output += arg
    self.idx += 1

  def jmp(self, arg):
    self.instdone[self.idx] = True
    self.idx += arg

  def process(self):
    while self.idx < len(self.inputs) and \
          not self.completed:
      if self.instdone[self.idx]:
        self.paused = True
        break

      inst = self.inputs[self.idx]
      op, arg = AccSimulator.parse(inst)
      if op == 'nop': self.noop()
      elif op == 'acc': self.acc(arg)
      elif op == 'jmp': self.jmp(arg)
      else:
       print(f"unknown: inst={inst} idx={self.idx}")
       break
    if not self.paused: self.completed = True
