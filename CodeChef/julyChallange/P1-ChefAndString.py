def chefAndString(list1):
    c = 0
    for i in range(len(list1)-1):
        c += (abs(list1[i+1]-list1[i])-1)
    return c




if __name__ == '__main__':
    testCases = int(input())
    if 1<= testCases<=10:
        while testCases:
            testCases -= 1
            G = int(input())
            j= list(map(int, input().split()))
            if 2<=G<=10**5:
                print(chefAndString(j))

