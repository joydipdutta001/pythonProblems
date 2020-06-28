def beautifullMatrix(arr):
    row,col,res=0,0,0

    for i in range(5):
        for j in range(5):
            if arr[i][j] == 1:
                row =i
                col =j
                break

    res += abs(2-row) + abs(2 - col)
    return res

if __name__ == '__main__':
    array = []
    for _ in range(5):
        array.append(list(map(int, input().rstrip().split())))
    print(beautifullMatrix(array))