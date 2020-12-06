import sys, functools, re


def part1(filename):
    with open(filename) as f:
        lines = [l.rstrip('\n') for l in f.readlines()]

    counts = []
    for l in lines:
        dec = bytearray(l, 'utf-8').decode('unicode_escape')
        strlen = len(l)
        # length of bytearray minus 2 quotes - quotes - double slashes
        declen = len(dec) - 2
        counts.append((strlen, declen))

    total = sum([c[0]-c[1] for c in counts])
    print(f"part1 >>> Santa's list of naughty/nice will be {total}")


def part2(filename):
    with open(filename) as f:
        lines = [l.rstrip('\n') for l in f.readlines()]

    counts = []
    for l in lines:
        strlen = len(l)
        # length of string + (2 quotes + 2 backslashes) + backslashes + quotes
        enclen = len(l) + 4 + l[1:-1].count('\\') + l[1:-1].count('"')
        counts.append((strlen, enclen))

    total = sum([c[1]-c[0] for c in counts])
    print(f"part2 >>> Santa's list of naughty/nice will be {total}")


if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
