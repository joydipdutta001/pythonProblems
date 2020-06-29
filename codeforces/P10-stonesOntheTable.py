def stonesOnTheTable(n,string):
    steps = 0
    for i in range(1,n):
        if string[i]==string[i-1]:
            steps +=1
    return steps

if __name__ == '__main__':
    n = int(input())
    string = input()
    if 1<=n<=50:
       print(stonesOnTheTable(n,string))
    else:
        raise ValueError