def isPrime(n):
    i = 2
    isPrime = True
    if n == 1:
        isPrime = False
    while i * i <= n:
        if n % i == 0:
            isPrime = False
            break
        i += 1
    return isPrime

def prediction(n, m):

    for i in range(n+1, m):

        if isPrime(i):
            return "NO"

    return "YES" if isPrime(m) else "NO"

if __name__ == '__main__':
    n,m = map(int,input().split(" "))
    if 2<=n<m<=50:
        print(prediction(n,m))
    else:
        raise ValueError