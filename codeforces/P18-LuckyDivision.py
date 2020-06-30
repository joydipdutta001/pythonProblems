def luckyDivision(n):
    c = 0
    n1 = n
    while (n != 0):
        r = n % 10
        if r != 4 and r != 7:
            c += 1
        n //= 10
    if c>0:
        if n1%4 == 0 or n1%7==0 or n1%47==0 or n1 % 74==0:
            return True
        else:
            return False
    else:
        return True

if __name__ == '__main__':
    n = int(input())
    if luckyDivision(n):
        print("YES")
    else:
        print("NO")