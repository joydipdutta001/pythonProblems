N = int(input())
while(100>=N>0):

    # count =0
    # i =0
    # f,b,t,d = input().strip().split(" ")
    # F,B,T,D = int(f),int(b),int(t),int(d)
    # if F>0 and B>0 and T>0 and D>0 and B>F:
    #     while(i<=(D-B)):
    #         i = i +(B-F)
    #         count+=1
    #
    #     time = (((B*T)+(F*T))*count)-(F*T)
    #     print(time)

    count = 0
    i = 0
    f, b, t, d = input().strip().split(" ")
    F, B, T, D = int(f), int(b), int(t), int(d)
    if F > 0 and B > 0 and T > 0 and D > 0 and B > F:
        while (0 < (D - B)):
            D -= B
            count += B
            if D > 0:
                D += F
                count += F
        count += D
        print(count * T)

    N-=1