# Simple Chessboard
#
# Write a program that prints a simple chessboard.
# Input format:
#
#     The first line contains the number of inputs T.
#     The lines after that contain a different values for size of the chessboard
#
# Output format:
#
# Print a chessboard of dimensions size * size. Print a Print W for white spaces and B for black spaces.
#
# Input:
# 2
# 3
# 5
#
# Output:
# WBW
# BWB
# WBW
# WBWBW
# BWBWB
# WBWBW
# BWBWB
# WBWBW
def simpleChessboard(t):

    while(t>0):
        n = int(input())
        for i in range(1,n+1):
            if(i%2!=0):
                c = 'W'
            else:
                c = 'B'
            for j in range(1,n+1):
                print(c,end="")
                if (c=='W'):
                    c = 'B'
                else:
                    c= 'W'
            print(end="\n")
        t -=1

t = int(input())
while t>0:
    n,char = input().split()


    for i in range(1,int(n)+1):

        c=char
        for j in range(1,int(n)+1):
            print(c,end="")
            if (c=='W'):
                c = 'B'
            else:
                c= 'W'

        print(end="\n")
        if (char == 'W'):
            char = 'B'
        else:
            char = 'W'
    t -=1