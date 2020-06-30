def reverseNum(num):

    reverse = 0

    while (num > 0):
        a = num % 10
        reverse = reverse * 10 + a
        num = num // 10

    return reverse

if __name__ == '__main__':
    t = int(input())
    numList = []
    if 1<=t<=1000:
        while (t>0):
            n = int(input())
            if 1<=n<=1000000:
                numList.append(n)
                t-=1
            else:
                raise ValueError
        for i in numList:
            print(reverseNum(i))
    else:
        raise ValueError
