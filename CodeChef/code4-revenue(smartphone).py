def revenueMax(lst1):
    lst = sorted(lst1)
    n=len(lst)
    result = 0
    for i in range(len(lst)):
        result = max(result,lst[i]*(n-i))
    return result

if __name__ == '__main__':
    N = int(input())
    array = []
    while(N>0):
        array.append(int(input()))
        N-=1
    print(revenueMax(array))