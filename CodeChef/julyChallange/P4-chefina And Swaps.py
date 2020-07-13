def chefina(l1,l2):
    count=0

    for i in range(len(l1)):
        l1[i]=l2[i]

        if sum(l1)==sum(l2):
            if sorted(l1)==sorted(l2):
                break
            else:
                count+=1
        else:
            count+=1
    print(l1,l2)
    if sum(l1)!=sum(l2):
        return -1
    else:
        return count









if __name__ == '__main__':
    testCases = int(input())
    if 1<= testCases<=2000:
        while testCases:
            testCases -= 1
            G = int(input())
            lst1=sorted(list(map(int,input().split())))
            lst2= sorted(list(map(int,input().split())))
            if len(lst1)>1:
                if lst1 != lst2:
                    print(chefina(lst1,lst2))
                else:
                    print(0)
            else:
                if lst1 == lst2:
                    print(0)
                else:
                    print(-1)

