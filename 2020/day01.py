import sys, functools

def part1(filename):
  with open(filename) as f:
    numbers = [int(l.rstrip('\n')) for l in f.readlines()]

  for i in range(0,len(numbers)-2):
    for j in range(1,len(numbers)):
      if numbers[i]+numbers[j] == 2020:
        mult = numbers[i]*numbers[j]
        print (f"values=[{numbers[i]}, {numbers[j]}], mult={mult}")
        return


def part2(filname):
  with open(filename) as f:
    numbers = [int(l.rstrip('\n')) for l in f.readlines()]

  for i in range(0,len(numbers)-3):
    for j in range(1,len(numbers)-2):
      for k in range(2,len(numbers)):
        if numbers[i]+numbers[j]+numbers[k] == 2020:
          mult = numbers[i]*numbers[j]*numbers[k]
          print (f"values=[{numbers[i]}, {numbers[j]}, {numbers[k]}], mult={mult}")
          return


if __name__ == "__main__":
  filename = sys.argv[1]
  part1(filename)
  part2(filename)
