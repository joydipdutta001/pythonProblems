 #//finding all prim numbers between 1 and N, inclusive
# // prime[i-1] is false if i is a prime number

def primeList(n):

    primLists=[2]
    for val in range(2, n + 1):
        if val > 1:
            for n1 in range(2, val // 2 + 2):

                if (val % n1) == 0:
                    break

                else:

                    if n1 == val // 2 + 1:

                        primLists.append(val)
    return primLists

print(primeList(17))
if __name__ == '__main__':

    n = int(input())
    primeLis = primeList(n)
    sum = 0
    primeCount =0
    for i in range(0,len(primeLis)):
        sum = sum +primeLis[i]
        print(sum)
        # print(str(primeLis[i])+"list")
        if (sum in primeLis):
            primeCount+=1
            continue
        elif (sum>primeLis[i]):
            continue
    print(primeCount)
    print(primeLis)

