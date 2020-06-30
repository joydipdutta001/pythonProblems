def twinsTwins(lst):
    lstSort = sorted(lst)
    sum = 0
    count1 = 0
    countFinal =0
    for i in lstSort:
        sum+=i
    for i in lstSort[::-1]:
        count1+=i
        countFinal+=1
        if count1 >(sum/2):
            break
    return countFinal

if __name__ == '__main__':
    n = input()
    lst1 = list(map(int, input().split(" ")))
    print(twinsTwins(lst1))