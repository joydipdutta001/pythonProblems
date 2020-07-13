
T = int(input())

while T:
    T -= 1
    N = int(input())
    P, Q = map(int, input().split(" "))

    numDecimal = str((abs(P/Q))-abs((P//Q)))[2:N+2]

    n = int(numDecimal)

    r = 0
    while (n >0):
        r += (n % 10)
        n //= 10
    print(r)


