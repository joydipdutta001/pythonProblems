
def head_triangle(t_rows):

    for i in range(1,t_rows+1):
        print(((t_rows)-i)*" ",end="")
        print((2*i-1)*"*")

def partial_triangle(t_rows,offsets):

    for j in range(1,t_rows+1):
        print(offsets * " ",end="")
        print((t_rows-j)*" ",end="")
        print((2*j+1)*"*")


def stand(t_rows):
    for i in range(0,2):
        print(t_rows*" ",end="")
        print("*",end="\n")

def tree(t_rows):
    head_triangle(t_rows + 1)
    for k in range(1, t_rows - 1):
        partial_triangle(t_rows - k, k)

    stand(t_rows)

if __name__ == '__main__':
    times = int(input())
    while times>0:
        n = int(input())
        if n<=1:
            print("You cannot generate christmas tree")

        elif n>=20:
            print("Tree is no more")
        else:
            tree(n)

        times -= 1
