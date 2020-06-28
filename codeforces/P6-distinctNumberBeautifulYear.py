import sys

INT_MAX = sys.maxsize

def countDistinct(n):
    arr = [0] * 10
    count = 0
    while (n != 0):
        r = int(n % 10)
        arr[r] = 1
        n //= 10

    for i in range(10):
        if (arr[i] != 0):
            count += 1

    return count


def countDigit(n):
    c = 0

    while (n != 0):
        r = n % 10
        c += 1
        n //= 10

    return c

def nextNumberDistinctDigit(n):
    while (n < INT_MAX):
        distinct_digits = countDistinct(n + 1)

        total_digits = countDigit(n + 1)

        if (distinct_digits == total_digits):


            return n + 1
        else:


            n += 1

    return -1



if __name__ == '__main__':
    n = int(input())

    print(nextNumberDistinctDigit(n))