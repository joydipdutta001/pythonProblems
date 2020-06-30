def gameSticks(n1,n2):
    minimum = min(n1,n2)
    if minimum % 2==0:
        return "Malvika"
    else:
        return "Akshat"

if __name__ == '__main__':
    num1,num2 = map(int,input().split(" "))
    print(gameSticks(num1,num2))
