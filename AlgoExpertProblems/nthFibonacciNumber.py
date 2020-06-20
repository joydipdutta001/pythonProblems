# O(2^n) time || O(n) space
def nthFib(n):
    if n == 2:
        return 1
    elif n== 1:
        return 0
    else:
        return nthFib(n-1) +nthFib(n-2)

# O(n) time || O(n) space
def nthFibmore(n, mem= {1:0,2:1}):
    if n in mem:
        return mem[n]
    else:
        mem[n]= nthFibmore(n-1, mem)+ nthFibmore(n-2,mem)
        return mem[n]


# O(n) time || O(1) space
def nthbetterfib(n):
    lastTwo = [0,1]
    count = 3
    while count<=n:
        nexFib = lastTwo[0]+ lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1]= nexFib
        count +=1
    return lastTwo[1] if n > 1 else lastTwo[0]

n = int(input("Enter the number:> "))

print(str(nthFib(n))+ " "+
str(nthFibmore(n))+" "+
str(nthbetterfib(n)))