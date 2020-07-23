import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    hrglasses = []
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    # print(arr)
    for i in range(4):
        for j in range(4):
            b1 = arr[j][i:i + 3]
            b2 = arr[j + 1][i + 1]
            b3 = arr[j + 2][i:i + 3]
            hrglass = sum(b1) + b2 + sum(b3)
            hrglasses.append(hrglass)
    print(max(hrglasses))
