total = int(input())

while total > 0:

    n = int(input())
    first = 2
    second = 1
    count = 0
    while count < n:
        print(first, end=" ")
        sum = first + second
        first = second
        second = sum
        count += 1
    print("")
    total -= 1