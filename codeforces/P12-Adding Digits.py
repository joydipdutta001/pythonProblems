
def addingDigits(a,b,n):
    a *= 10
    for i in range(10):
        if (a + i) % b == 0:
            return str(a + i) + "0" * (n - 1)

    return -1

if __name__ == '__main__':
    a, b, n = map(int, input().split(" "))
    print(addingDigits(a,b,n))