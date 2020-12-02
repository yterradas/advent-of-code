import sys, functools

def part1(filename):
    with open(filename) as f:
        parans = f.readline().rstrip('\n')

    u = parans.count('(');
    d = parans.count(')');
    print(f"part1 >>> Santa goes to floor={u-d}")

    
def part2(filename):
    with open(filename) as f:
        parans = f.readline().rstrip('\n')

    n = 0
    for i, v in enumerate(parans):
        if v == '(': n += 1
        if v == ')': n -= 1
        if n == -1:
            print(f"part2 >>> Santa first enters the basement on {i+1}")
            break
        

if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
