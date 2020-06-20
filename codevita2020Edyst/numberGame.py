import math



def prime(n):
    primeList = []
    while n % 2 == 0:
        primeList.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            primeList.append(i)
            n = n / i
    if n > 2:
        primeList.append(int(n))
    return primeList



if __name__ == '__main__':

    N = int(input())
    numbers = [int(n) for n in input().strip().split(" ")]

    lenPrimeList = [len(prime(num)) for  num in numbers]

    ct= 0
    for j in lenPrimeList:
        ct = ct ^ j

    if ct == 0:
        print("JASBIR")
    else:
        print("AMAN")


