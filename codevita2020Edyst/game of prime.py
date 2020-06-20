def isHappy(n):
    sum = 0
    isHapp=True
    while(n>0):
        sum += (n%10)*(n%10)
        # print(sum)
        n = n//10
        if sum == 1:
            return isHapp

        elif sum == 4:
            isHapp= False
            return isHapp
        break

    isHappy(sum)


# num = 11

#
# def isHappyNumber(num):
#     sum = 0
#
#     while (num > 0):
#         rem = num % 10
#         sum = sum + (rem * rem)
#         num = num // 10
#
#
#     while (sum != 1 and sum != 4):
#         sum = isHappyNumber(sum)
#
#     if (sum == 1):
#         return True
#
#     elif (sum == 4):
#         return False



def isPrime(n):
    i = 2
    isPrime = True
    while i * i <= n:
        if n % i == 0:
            isPrime = False
            break
        i+=1


    return isPrime


# print(isPrime(int(input())))
print(isHappy(17))
print(isPrime(15))