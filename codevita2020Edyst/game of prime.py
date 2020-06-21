# def isHappy(n):
#     sum = 0
#
#     while(n>0):
#         sum += (n%10)*(n%10)
#         # print(sum)
#         n = n//10
#     if sum == 1:
#         return True
#
#     elif sum == 4:
#         return False
#
#     return isHappy(sum)
#
#
#
#
# # num = 11
#
# #
# # def isHappyNumber(num):
# #     sum = 0
# #
# #     while (num > 0):
# #         rem = num % 10
# #         sum = sum + (rem * rem)
# #         num = num // 10
# #
# #
# #     while (sum != 1 and sum != 4):
# #         sum = isHappyNumber(sum)
# #
# #     if (sum == 1):
# #         return True
# #
# #     elif (sum == 4):
# #         return False
#
#
#
# def isPrime(n):
#     i = 2
#     isPrime = True
#     if n == 1:
#         isPrime =False
#     while i * i <= n:
#         if n % i == 0:
#             isPrime = False
#             break
#         i+=1
#
#
#     return isPrime
#
#
# # print(isPrime(int(input())))
# if __name__ == '__main__':
#
#     x = int(input())
#     y = int(input())
#     n = int(input())
#     if x <= y and x > 0 and y >0:
#
#         count = 1
#
#         for i in range(x,y):
#
#             if isHappy(i)==isPrime(i)==True:
#
#                 if count ==n:
#                     print(i)
#                 count += 1
#             else:
#                 print("No number is present at this index")
#     else:
#         print("Invalid Input")
#
#     # print("No number found")
def isHappy(n):
    sum = 0
    while (n > 0):
        sum += (n % 10) * (n % 10)
        n = n // 10
    if sum == 1:
        return True

    elif sum == 4:
        return False

    return isHappy(sum)


def isPrime(n):
    i = 2
    isPrime = True
    if n == 1:
        isPrime = False
    while i * i <= n:
        if n % i == 0:
            isPrime = False
            break
        i += 1
    return isPrime


if __name__ == '__main__':

    try:
        x = int(input())
        y = int(input())
        n = int(input())

        if x <= y and x > 0 and n > 0:

            count = 0

            for i in range(x, y + 1):

                if isHappy(i) == isPrime(i) == True:
                    count += 1
                    if count == n:
                        print(i)

                    elif count == 0:
                        print("No number is present at this index")
        else:
            print("Invalid Input")

    except ValueError:
        print("Invalid Input")


