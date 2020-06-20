def digit(pos):
    first, second = 6,28
    next2 = 0
    if pos == 1:
        return first
    elif pos == 2:
        return second
    else:
        for p in range(2,pos):
            next2 = (second*2)-first +16

            first = second
            second = next2
        return next2


if __name__ == '__main__':

    times = int(input())
    while times>0:
        n = int(input())
        i = 1
        for row in range(1,n+1):
            print((n-row)*"   ",end="")
            for j in range(0,row):
                print(format(digit(i),'05')+" ",end="")
                i+=1
            print(end="\n")
        times -=1