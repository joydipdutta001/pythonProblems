#
# def combineM(n):
#     l1,l2=[],[]
#     for i in range(1,n+1):
#         l1.append(i*((2*i)-1))
#         l2.append(i*(i+1)//2)
#
#     if set(l1)&set(l2):
#         n_list=sorted(set(l1)&set(l2))
#         return n_list
#
# if __name__ == '__main__':
#
#     n1,n2,m= input().split()
#     n1,n2,m = int(n1),int(n2),int(m)
#     out = []
#     for i in combineM(1000):
#         if n1<= i <=n2:
#             out.append(i)
#     print(out[m-1])
#

def bet(T1,T2,M):

  As=1

  i=1

  lst=[]

  if(int(T1)<=0 or int(T2)<=0 or M.isalpha()):

    return "Invalid Input"

  else:

    while(As<=int(T2)):

      As=i*(2*i-1)

      if(As>=int(T1) and As<=int(T2)):

        lst.append(As)

      i+=1

    if(len(lst)>=int(M)):

      return lst[int(M)-1]

    else:

      return "No number is present at this index"


T1,T2,M=map(str,input().split())

print(bet(T1,T2,M))


