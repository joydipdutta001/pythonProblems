# cook your dish here
array=[]
while(True):

    n = int(input())
    if n==42:
        for i in array:
            print(i)
        break
    else:
        array.append(n)
