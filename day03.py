import sys,math

def bpath(port, n1):
  board = []
  p1 = port
  for c in n1:
    direction = c[0]
    distance = int(c[1:])
    if direction == 'L':
      points = [(p1[0] - i, p1[1]) for i in range(distance)]
      board += points
      p1 = (p1[0] - distance, p1[1])
    if direction == 'R':
      points = [(p1[0] + i, p1[1]) for i in range(distance)]
      board += points
      p1 = (p1[0] + distance, p1[1])
    if direction == 'D':
      points = [(p1[0], p1[1] - i) for i in range(distance)]
      board += points
      p1 = (p1[0], p1[1] - distance)
    if direction == 'U':
      points = [(p1[0], p1[1] + i) for i in range(distance)]
      board += points
      p1 = (p1[0], p1[1] + distance)
  return board

def manhattan(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def part1(filename='in03.txt'):
  with open(filename) as f:
    path1 = f.readline().rstrip('\n').split(',')
    path2 = f.readline().rstrip('\n').split(',')
    port = (0, 0)
    board1 = bpath(port, path1)
    board2 = bpath(port, path2)
    insk = set(board1).intersection(set(board2))
    s = math.inf
    p = port
    for i in insk:
      if i[0] == 0 and i[1] == 0: continue
      d = manhattan(port, i)
      print(f"point: {i}, distance: {d}")
      if d < s:
        s = d
        p = i
    print(f"output part1: point={p}, distance={s}")

def part2(filename='in03.txt'):
  with open(filename) as f:
    path1 = f.readline().rstrip('\n').split(',')
    path2 = f.readline().rstrip('\n').split(',')
    port = (0, 0)
    board1 = bpath(port, path1)
    board2 = bpath(port, path2)
    insk = set(board1).intersection(set(board2))
    s = math.inf
    p = port
    for i in insk:
      if i[0] == 0 and i[1] == 0: continue
      d = manhattan(port, i)
      print(f"point: {i}, distance: {d}")
      if d < s:
        s = d
        p = i
    print(f"output part2: point={p}, steps path A={board1.index(p)}, steps path B={board2.index(p)}")

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
