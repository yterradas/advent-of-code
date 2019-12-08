import fileinput
import sys

def part1(filename, width, height):
  with open(filename) as f:
    line = f.readline().rstrip('\n')
    lsize = width * height
    layers = [line[i:i+lsize] for i in range(0, len(line), lsize)]
    least0 = [l.count('0') for l in layers]
    l0 = layers[least0.index(min(least0))]
    n1 = l0.count('1')
    n2 = l0.count('2')
    print(f"output part1: image with fewer '0', nof '1' x nof '2' = {n1*n2}")

def part2(filename, width, height):
  with open(filename) as f:
    line = f.readline().rstrip('\n')
    lsize = width * height
    layers = [line[i:i+lsize] for i in range(0, len(line), lsize)]

    image = ''
    for i in range(lsize):
      pixels = [layers[j][i] for j in range(len(layers))]
      for p in pixels:
        if p == '2': continue
        image += p
        break

    print(f"output part2: final image")
    image = image.replace('0', ' ').replace('1', '#')
    [print(image[i:i+width]) for i in range(0, len(image), width)]


if __name__ == "__main__":
  filename = sys.argv[1]
  width = int(sys.argv[2])
  height = int(sys.argv[3])

  part1(filename, width, height)
  part2(filename, width, height)
