
def countDigit(n):
    c = 0

    while (n != 0):
        r = n % 10
        if r == 4 or r == 7:
            c += 1
        n //= 10
    if c>0:
        if c == 4 or c == 7:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


if __name__ == '__main__':
    n = int(input())
    if 1<= n <= (10**18):
        print(countDigit(n))
    else:
        raise ValueError