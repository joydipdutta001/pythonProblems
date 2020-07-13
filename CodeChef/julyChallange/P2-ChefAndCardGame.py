def isChef(chef,morty):
    a,c = 0,0
    while (chef > 0)or(morty>0):
        a += chef % 10
        c += morty %10

        chef = chef // 10
        morty = morty //10
    if a >c:
        return 1
    elif a == c:
        return 2
    else:
        return 0


if __name__ == '__main__':
    testCases = int(input())
    if 1<= testCases<=1000:
        while testCases:
            testCases -= 1
            G = int(input())
            chef1=0
            morty1=0
            while G:
                G-=1
                j, t = map(int, input().split())
                if isChef(j,t) ==1:
                    chef1 +=1
                elif isChef(j,t)==0:
                    morty1 +=1
                else:
                    chef1+=1
                    morty1+=1
            if chef1>morty1:
                print("{} {}".format(0,chef1))
            elif chef1< morty1:
                print("{} {}".format(1,morty1))
            else:
                print("{} {}".format(2,chef1))


