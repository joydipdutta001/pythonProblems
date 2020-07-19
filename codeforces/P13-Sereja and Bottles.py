def serejaAndBottles(n):
    count = 0
    while(n>0):

        a,b = map(int, input().split(" "))
        if a == b:
            count+=1
        n-=1
    return count

n = int(input())
print(serejaAndBottles(n))