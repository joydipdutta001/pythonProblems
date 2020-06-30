def coinFlips(i1,n1,q1):
    if n1 % 2 == 0:
        return n1 // 2
    else:
        if i1 == q1:
            return n1 // 2
        else:
            return (n1 // 2) + 1

if __name__ == '__main__':
    testCases = int(input())
    while testCases:
        testCases -= 1
        G = int(input())
        while G:
            G -= 1
            i, n, q = map(int, input().split())
            print(coinFlips(i,n,q))