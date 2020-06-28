num,t1=input().split()
t = int(t1)
array = list(input())

while(t>0):
    i=0

    while i<(len(array)-1):
        if array[i]=='B' and array[i+1]=='G':
            array[i],array[i+1] = array[i+1],array[i]

            i+=1
        i+=1
    t-=1

stringOut = ""
for j in range(len(array)):
    stringOut += array[j]

print(stringOut)

