 #//finding all prim numbers between 1 and N, inclusive
# // prime[i-1] is false if i is a prime number

# def primeList(n):
#
#     primLists=[2]
#     for val in range(2, n + 1):
#         if val > 1:
#             for n1 in range(2, val // 2 + 2):
#
#                 if (val % n1) == 0:
#                     break
#
#                 else:
#
#                     if n1 == val // 2 + 1:
#
#                         primLists.append(val)
#     return primLists

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

if __name__ == '__main__':

    k = 1
    while k > 0:
        n = int(input())
        primeLis = [i for i in range(1, n + 1) if isPrime(i)]
        print(primeLis)
        primeCount = 0
        for i in range(1, len(primeLis)):
            sum = 0
            for j in range(0, len(primeLis) - 1):
                sum = sum + primeLis[j]
                if sum == primeLis[i]:
                    primeCount += 1
                elif sum > primeLis[i]:
                    break
        print(primeCount)
        k -= 1


