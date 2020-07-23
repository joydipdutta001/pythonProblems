def carvans(ncars,carspeeds):
    maxspeed = carspeeds[0]
    count = 0
    for i in range(1, len(carspeeds)):
        if carspeeds[i] > maxspeed:
            count += 1
        else:
            maxspeed = carspeeds[i]
    return ncars - count

if __name__ == '__main__':
    t = int(input())
    if 1<=t<=100:
        while t:
            t -= 1
            n = int(input())
            if 1<=n<=10000:
                nspeeds = list(map(int, input().split(" ")))
                print(carvans(n, nspeeds))


