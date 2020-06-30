def presents(num,lst):
    lst1 = [0]*num
    for i in range(num):
        lst1[lst[i]-1]= i+1
    for j in lst1:
        print(j,end=" ")

if __name__ == '__main__':
    n = int(input())
    ls = list(map(int,input().split(" ")))
    presents(n,ls)
