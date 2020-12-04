import sys, functools
import hashlib

def part1(filename):
    with open(filename) as f:
        lines = [l.rstrip('\n') for l in  f.readlines()]

    nicestr = 0
    for line in lines:
        prevlet = ''
        vowelcount = 0
        consecutivelet = 0
        badseq = 0
        for letter in line:
            if (letter == 'b' and prevlet == 'a') or \
               (letter == 'd' and prevlet == 'c') or \
               (letter == 'q' and prevlet == 'p') or \
               (letter == 'y' and prevlet == 'x'): badseq = 1
            if letter == prevlet: consecutivelet = 1
            if letter in 'aeiou': vowelcount += 1
            prevlet = letter
        if vowelcount >= 3 and consecutivelet == 1 and badseq == 0:
            nicestr += 1

    print(f"part1 >>> Santa has {nicestr} strings")


def part2(filename):
    with open(filename) as f:
        lines = [l.rstrip('\n') for l in  f.readlines()]

    nicestr = 0
    for line in lines:
        duplicatelet = False
        for a,b in zip(line[0::],line[1::]):
            if line.count(a+b) >= 2:
                duplicatelet = True
                break

        inbetwenlet = False
        for a,b in zip(line[0::],line[2::]):
            if a == b:
                inbetwenlet = True
                break

        if duplicatelet and inbetwenlet:
            nicestr += 1

    print(f"part2 >>> Santa has {nicestr} strings")


if __name__ == "__main__":
    filename = sys.argv[1]
    part1(filename)
    part2(filename)
