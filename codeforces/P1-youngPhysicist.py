def youngPhysicist(arr):
    c,d,e= 0,0,0
    for i in range(len(arr)):
        c += arr[i][0]
        d += arr[i][1]
        e += arr[i][2]

    if c==0 and d == 0 and e == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':

    arr = []
    for _ in range(int(input())):
        arr.append(list(map(int, input().rstrip().split())))
    print(youngPhysicist(arr))