import fileinput, sys
from collections import namedtuple, defaultdict

def part1(filename='in03.txt'):
  Point = namedtuple('Point', ['x', 'y'])
  paths = []
  with fileinput.input(filename) as f:
    paths.append(f.readline().split(','))
    paths.append(f.readline().split(','))
    process(Point(1000, 1000), paths)

def part2(filename='in03.txt'):
  pass

def process(port, paths):
  board = [['-' for i in range(port.y*2)] for j in range(port.x*2)]
  board[port.y][port.x] = 'o'
  p1 = port
  for c in paths[0]:
    direction = c[0]
    distance = int(c[1:])
    if direction = 'L':
      p2 = Point(p1.x - distance, p1.y)
      board[p2.y][p2.x] = '+'
      for i in range(1, p1.x - p2.x): board[p1.y][p1.x - p2.x] = '-'
    elif direction = 'R':
      p2 = Point(p1.x + distance, p1.y)
      board[p2.y][p2.x] = '+'
      for i in range(p1.x, p1.x + distance): board[p1.y][p1.x + p2.x] = '-'
    elif direction = 'D':
      p2 = Point(p1.x, p1.y + distance)
      board[p2.y][p2.x] = '+'
      # TODO
      for i in range(p1.y, p2.y): board[p1.y][p1.x] = '-'

    elif direction = 'U':
      pass
    p1 = Point(p1.x - distance, p1.y)
  print(f"Central port is located@({port.x}, {port.y})")
  print_board(board)

def print_board(board):
  for r in board:
    print(r)

def manhattan_distance(p1, p2):
  return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def line_intersection(p1, p2, p3, p4):
  a1 = p1.y - p2.y
  b1 = p2.x - p1.x
  c1 = -(p1.x * p2.y - p2.x * p1.y)

  a2 = p3.y - p4.y
  b2 = p4.x - p3.x
  c2 = -(p3.x * p4.y - p4.x * p3.y)

  d = a1 * b2 - b1 * a2
  dx = c1 * b2 - b1 * c2
  dy = a1 * c2 - c1 * a2

  if d != 0:
    x = dx / d
    y = dy / d
    return Point(x, y)
  else:
    return False

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
