import sys, functools

def direction(currdir, pos):
    if currdir == '>': return (pos[0]+1,pos[1])
    if currdir == '<': return (pos[0]-1,pos[1])
    if currdir == '^': return (pos[0],pos[1]+1)
    if currdir == 'v': return (pos[0],pos[1]-1)


def part1(filename):
    with open(filename) as f:
        directions = f.readline().rstrip('\n')

    pos = (0,0)
    grid = {pos}
    for currdir in directions:
        pos = direction(currdir, pos)
        grid.add(pos)

    housesvisited = len(grid)
    print(f"part1 >>> Santa delivers at least 1 present to {housesvisited} houses")

    
def part2(filename):
    with open(filename) as f:
        directions = f.readline().rstrip('\n')

    santapos = (0,0)
    robosantapos = (0,0)
    grid = {(0,0)}
    for santadir, robosantadir in zip(directions[0::2], directions[1::2]):
        santapos = direction(santadir, santapos)
        grid.add(santapos)
        robosantapos = direction(robosantadir, robosantapos)
        grid.add(robosantapos)

    housesvisited = len(grid)
    print(f"part2 >>> Santa & Robo-Santa deliver at least 1 present to {housesvisited} houses")


if __name__ == "__main__":
    filename = sys.argv[1]
    part1(filename)
    part2(filename)
