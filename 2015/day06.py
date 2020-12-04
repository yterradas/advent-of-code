import sys, functools

def parseinst(line):
    l = line.split(' ')
    if len(l) == 4:
        return l[0], \
            (int(l[1].split(',')[0]), int(l[1].split(',')[1])), \
            (int(l[3].split(',')[0]), int(l[3].split(',')[1]))
    else:
        return l[1], \
            (int(l[2].split(',')[0]), int(l[2].split(',')[1])), \
            (int(l[4].split(',')[0]), int(l[4].split(',')[1]))


def part1(filename):
    with open(filename) as f:
        lines = [l.rstrip('\n') for l in f.readlines()]

    grid = [[0 for i in range(1000)] for j in range(1000)]
    for line in lines:
        inst, spair, epair = parseinst(line)
        #print(spair, epair, inst)

        for y in range(spair[0], epair[0]+1):
            for x in range(spair[1], epair[1]+1):
                if inst == 'off':
                    grid[x][y] = 0
                elif inst == 'on':
                    grid[x][y] = 1
                else:
                    grid[x][y] ^= 1

    lightslit = sum([grid[x][y] for x in range(0,1000) for y in range(0,1000)])
    print(f"part1 >>> Santa says lit {lightslit} lights")


def part2(filename):
    with open(filename) as f:
        lines = [l.rstrip('\n') for l in f.readlines()]

    grid = [[0 for i in range(1000)] for j in range(1000)]
    for line in lines:
        inst, spair, epair = parseinst(line)
        #print(spair, epair, inst)

        for y in range(spair[0], epair[0]+1):
            for x in range(spair[1], epair[1]+1):
                if inst == 'off':
                    if grid[x][y] > 0: grid[x][y] -= 1
                elif inst == 'on': grid[x][y] += 1
                else: grid[x][y] += 2

    brightness = sum([grid[x][y] for x in range(0,1000) for y in range(0,1000)])
    print(f"part2 >>> Santa says set brightness to {brightness}")


if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
