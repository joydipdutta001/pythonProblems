""" 
////////////////////////////////////////////////////////////////////////////////
                author_name= Joydip Dutta,
                author_email= duttajoydip98@gmail.com,
                github_id = joydipdutta001
                linkedIn_id = Joydip Dutta (JD)
                Website = cybotians.com

                Problem No. = Day-20
                

                
                
 ////////////////// THANK YOU /////////////////////////////////////////////////   
 """


def SwapNum(n, alist):
    swaps = 0
    for i in range(0,n):
        for j in range(0, n-1):
            if (alist[j] > alist[j + 1]):
                c = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = c
                swaps += 1
        if (swaps == 0):
            break
    return swaps, alist

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    numberOfSwaps,sortedList  = SwapNum(n,a)

    print("Array is sorted in {} swaps.".format(numberOfSwaps))
    print("First Element: " + str(sortedList[0]))
    print("Last Element: " + str(sortedList[n - 1]))