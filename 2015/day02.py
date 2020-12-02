import sys, functools

def part1(filename):
    with open(filename) as f:
        lines = [[int(i) for i in l.rstrip('\n').split('x')] for l in f.readlines()]

    paperneed = 0
    for (l,w,h) in lines:
        s1 = l*w
        s2 = w*h
        s3 = h*l
        surfaceext = 2*(s1 + s2 + s3) + min(s1,s2,s3)
        paperneed += surfaceext
        #print(f"l={l}, w={w}, h={h}, area+extra={surfaceext}")
        
    print(f"part1 >>> Elfs need {paperneed} sqr feet of wrapping paper")

    
def part2(filename):
    with open(filename) as f:
        lines = [[int(i) for i in l.rstrip('\n').split('x')] for l in f.readlines()]

    ribbonneed = 0
    for line in lines:
        line.sort()
        l, w, h = line[0], line[1], line[2]
        ribbonext = l*w*h + 2*l + 2*w
        ribbonneed += ribbonext
        #print(f"l={l}, w={w}, h={h}, tie+bow={ribbonext}")
        
    print(f"part1 >>> Elfs need {ribbonneed} sqr feet of ribbon")


if __name__ == "__main__":
    filename = sys.argv[1]
    part1(filename)
    part2(filename)
