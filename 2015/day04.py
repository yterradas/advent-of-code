import sys, functools
import hashlib

def part1(filename):
    with open(filename) as f:
        secret = f.readline().rstrip('\n')

    i = 1
    while True:
        str2hash = f"{secret}{i}"
        result = hashlib.md5(str2hash.encode()) 
        h = result.hexdigest()
        if h[0:5] == '00000': break
        i += 1
        
    print(f"part1 >>> Santa's lowest positive number with hx00000 is {i}")

    
def part2(filename):
    with open(filename) as f:
        secret = f.readline().rstrip('\n')

    i = 1
    while True:
        str2hash = f"{secret}{i}"
        result = hashlib.md5(str2hash.encode()) 
        h = result.hexdigest()
        if h[0:6] == '000000': break
        i += 1
        
    print(f"part2 >>> Santa's lowest positive number with hx000000 is {i}")


if __name__ == "__main__":
    filename = sys.argv[1]
    part1(filename)
    part2(filename)
