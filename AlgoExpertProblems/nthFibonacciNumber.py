def nthFib(n):
    if n == 2:
        return 1
    elif n== 1:
        return 0
    else:
        return nthFib(n-1) +nthFib(n+2)

