

def isOdd(num):
    if num % 2 ==0:
        return False
    else:
        return True






if __name__ == '__main__':
    testCases = int(input())
    if 1<= testCases<=10:
        while testCases:
            testCases -= 1
            N = int(input())
            numList= list(map(int, input().split()))
            if 1<=N<=10**3:
                result = 1
                for i in numList:
                    result = result * i
                if isOdd(result):
                    print("YES")
                else:
                    print("NO")