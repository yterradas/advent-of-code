import sys, functools

def calccharmem(line):
    pass


def calccharnum(line):
    pass


def part1(filename):
    with open(filename) as f:
        lines = [l.rstrip('\n') for l in f.readlines()]

    # encoding is not done correctly
    # need to show utf8 before stripping quotes

        
    #.encode('utf-8').decode('unicode_escape')
    #counts = [(len(l), len(l.strip('\"')), l) for l in lines]
    #len(bytearray(l.strip('\"'), 'utf-8').decode("unicode_escape"))
    counts = []
    for l in lines:
        print("processing >>", l)
        enc = str(l.strip('\"'))
        counts.append((len(l), len(enc), l))

    [print(c) for c in counts]
    #[print(l) for l in counts]
    total = 0
    for c in counts:
        total += c[0] - c[1]

    print(f"part1 >>> Santa's list of naughty/nice will be {total}")


def part2(filename):
    pass


if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
