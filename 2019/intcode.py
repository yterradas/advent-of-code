class IntCode:
  def __init__(self, inputs, idx, rbase, debug=False):
    self.inputs = inputs
    self.outputs = []
    self.idx = idx
    self.rbase = rbase
    self.paused = False
    self.completed = False
    self.debug = debug

  @staticmethod
  def parse(n):
    modes = [int(i) for i in str(n//100).zfill(3)]
    op = n % 100
    return modes, op

  def modeidx(self, mode):
    if mode == 0:
      return self.inputs[self.idx]
    elif mode == 1:
      return self.idx
    elif mode == 2:
      return self.inputs[self.idx] + self.rbase
    else:
      print(f"unknown mode={mode}")

  def modeval(self, mode):
    i = self.modeidx(mode)
    return self.inputs[i]

  def op01(self, modes):
    i1 = self.modeval(modes[2])
    self.idx += 1
    i2 = self.modeval(modes[1])
    self.idx += 1
    i3 = self.modeidx(modes[0])
    self.idx += 1
    self.inputs[i3] = i1 + i2

  def op02(self, modes):
    i1 = self.modeval(modes[2])
    self.idx += 1
    i2 = self.modeval(modes[1])
    self.idx += 1
    i3 = self.modeidx(modes[0])
    self.idx += 1
    self.inputs[i3] = i1 * i2

  def op03(self, modes, uinputs):
    if len(uinputs) == 0:
      self.paused = True
      self.idx -= 1
    else:
      i1 = self.modeidx(modes[2])
      self.idx += 1
      self.inputs[i1] = uinputs.pop(0)

  def op04(self, modes):
    o = self.modeval(modes[2])
    self.idx += 1
    self.outputs.append(o)

  def op05(self, modes):
    i1 = self.modeval(modes[2])
    self.idx += 1
    i2 = self.modeval(modes[1])
    self.idx += 1
    if i1 != 0: self.idx = i2

  def op06(self, modes):
    i1 = self.modeval(modes[2])
    self.idx += 1
    i2 = self.modeval(modes[1])
    self.idx += 1
    if i1 == 0: self.idx = i2

  def op07(self, modes):
    i1 = self.modeval(modes[2])
    self.idx += 1
    i2 = self.modeval(modes[1])
    self.idx += 1
    i3 = self.modeidx(modes[0])
    self.idx += 1
    self.inputs[i3] = 1 if i1 < i2 else 0

  def op08(self, modes):
    i1 = self.modeval(modes[2])
    self.idx += 1
    i2 = self.modeval(modes[1])
    self.idx += 1
    i3 = self.modeidx(modes[0])
    self.idx += 1
    self.inputs[i3] = 1 if i1 == i2 else 0

  def op09(self, modes):
    o = self.modeval(modes[2])
    self.idx += 1
    self.rbase += o

  def op99(self):
    self.completed = True
    if self.debug: print("halting...")

  def resume(self):
    self.outputs = []
    self.paused = False

  def process(self, uinputs):
    while self.idx < len(self.inputs) and \
          not self.completed and \
          not self.paused:
      modes, op = IntCode.parse(self.inputs[self.idx])
      if self.debug:
        print(f"modes={modes}, op={op}, idx={self.idx}")
      self.idx += 1

      if op == 99: self.op99()
      elif op == 1: self.op01(modes)
      elif op == 2: self.op02(modes)
      elif op == 3: self.op03(modes, uinputs)
      elif op == 4: self.op04(modes)
      elif op == 5: self.op05(modes)
      elif op == 6: self.op06(modes)
      elif op == 7: self.op07(modes)
      elif op == 8: self.op08(modes)
      elif op == 9: self.op09(modes)
      else:
       print(f"unknown: modes={modes}, op={op}, idx={self.idx}, inputs={self.inputs}")
       break
