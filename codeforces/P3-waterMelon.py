def isEven(n):
    if n%2==0 and n>2:
        return True

    else:
        return False

if __name__ == '__main__':
    n= int(input())
    if isEven(n):
        print("YES")
    else:
        print("NO")






